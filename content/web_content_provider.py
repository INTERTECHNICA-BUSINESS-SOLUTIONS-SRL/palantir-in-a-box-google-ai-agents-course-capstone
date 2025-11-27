import requests
import re

from typing import Dict, Tuple
from datetime import datetime
from document_database import DocumentDatabase

from content.provider import ContentProvider
from document_database import DocumentDatabase

class WebContentProvider(ContentProvider):
    """
    Concrete implementation of the ContentProvider interface.
    """
    
    _DOCUMENT_STORAGE = "./0_0_2_cache/0_0_1_raw"
    
    def __init__(self):
        """
        Initializes the content provider system.
        """
        super().__init__()
        self._document_database = DocumentDatabase.get_implementation(self._DOCUMENT_STORAGE)

    def retrieve(self, url: str) -> Tuple[Dict[str, any], str]:
        """
        Obtains the content and associated properties for the provided URL.

        Args:
            url (str): The location identifier for the resource.

        Returns:
            Tuple[Dict[str, any], str]: A tuple containing the document metadata and document content.

        Raises:
            Exception: If the content cannot be obtained from the source.
        """
        # Check for existing record
        if self._document_database.has(url):
            return self._document_database.get(url)

        # Acquire content from remote source
        response = requests.get(url)
        
        if response.status_code == 200:
            content = response.text
            
            # Prepare metadata container
            metadata = {}
            
            # Derive document title from content
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if title_match:
                metadata['title'] = title_match.group(1).strip()
            else:
                metadata['title'] = "Untitled"

            # Derive timestamp from source information
            if 'Last-Modified' in response.headers:
                metadata['time'] = response.headers['Last-Modified']
            elif 'Date' in response.headers:
                metadata['time'] = response.headers['Date']
            else:
                metadata['time'] = str(datetime.now())

            # Store content and metadata for future access
            self._document_database.insert(url, metadata, content)
            
            return (metadata, content)
        else:
            raise Exception(f"Failed to retrieve content from {url}. Status: {response.status_code}")
