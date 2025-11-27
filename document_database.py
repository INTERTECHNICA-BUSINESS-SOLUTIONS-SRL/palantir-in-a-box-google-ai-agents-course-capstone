import os
from abc import ABC, abstractmethod
from typing import Dict, Tuple
from tinydb import TinyDB, Query
from uuid import uuid4

class DocumentDatabase(ABC):
    """
    Abstract Base Class defining the interface for a document database system.
    
    This interface mandates a contract for checking existence, retrieving, 
    and inserting documents and their associated metadata using unique identifiers.
    """
    
    # Internal configuration constants for storage keys and file names
    _DOCUMENT_DATABASE_CONTENT = "content"
    _DOCUMENT_DATABASE_FILE = "index.json"

    _KEY_ID = "id"
    _KEY_FILE_NAME = "file_name"
    _KEY_METADATA = "metadata"

    def __init__(self, database_directory: str):
        """
        Configures the storage location for the database instance.

        Args:
            database_directory (str): The filesystem path where documents and indices will be stored.
        """
        super().__init__()
        self._database_directory = database_directory

    @abstractmethod
    def has(self, key: str) -> bool:
        """
        Determines if a document exists in the persistence layer.

        Args:
            key (str): The unique identifier of the document.

        Returns:
            bool: True if the document exists, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Tuple[Dict[str, any], str]:
        """
        Retrieves a document's metadata and raw content.

        Args:
            key (str): The unique identifier of the document.

        Returns:
            Tuple[Dict[str, any], str]: A tuple containing the metadata dictionary and the content string.

        Raises:
            Exception: If the document identifier does not exist.
        """
        raise NotImplementedError

    @staticmethod
    def get_implementation(database_directory: str) -> 'DocumentDatabase':
        """
        Factory method to obtain the active database instance.

        Args:
            database_directory (str): The filesystem path where documents and indices will be stored.

        Returns:
            DocumentDatabase: An instance of the concrete database implementation.
        """
        return _TinyDBDocumentDatabase(database_directory)

    
class _TinyDBDocumentDatabase(DocumentDatabase) :
    """
    Concrete implementation of the DocumentDatabase interface.
    """

    def __init__(self, database_directory: str):
        """
        Initializes the persistence layer using the configured directory.
        
        Ensures the required directory structure exists and establishes 
        a connection to the data index.

        Args:
            database_directory (str): The filesystem path where documents and indices will be stored.
        """
        super().__init__(database_directory)
        
        # Ensure the root database directory exists
        if not os.path.exists(self._database_directory):
            os.makedirs(self._database_directory)
        
        # Ensure the content subdirectory exists
        if not os.path.exists(self._database_directory + "/" + self._DOCUMENT_DATABASE_CONTENT):
            os.makedirs(self._database_directory + "/" + self._DOCUMENT_DATABASE_CONTENT)
            
        # Establish the connection to the internal storage handler
        self._db = TinyDB(self._database_directory + "/" + self._DOCUMENT_DATABASE_FILE)

    def _get_database(self) -> TinyDB:
        """
        Retrieves the internal storage handler.

        Returns:
            TinyDB: The active handle to the internal storage mechanism.
        """
        return self._db

    def _get_query_by_id(self, id: str) -> Query:
        """
        Constructs a query object to locate a record by its unique ID.

        Args:
            id (str): The unique identifier to filter by.

        Returns:
            Query: A configured query object targeting the specified ID.
        """
        query = Query()
        return query[self._KEY_ID]

    def has(self, id: str) -> bool:
        """
        Checks if the document identifier is currently stored.

        Args:
            id (str): The unique identifier of the document.

        Returns:
            bool: True if the document exists, False otherwise.
        """
        database = self._get_database()
        query = self._get_query_by_id(id)
        results = database.search(query == id)
        
        return len(results) != 0

    def get(self, id: str) -> Tuple[Dict[str, any], str]:
        """
        Retrieves the stored document and its properties based on the identifier.

        Args:
            id (str): The unique identifier of the document.

        Returns:
            Tuple[Dict[str, any], str]: A tuple containing the metadata dictionary and the raw content string.
            
        Raises:
            Exception: If the provided identifier matches no existing record.
        """
        database = self._get_database()
        query = self._get_query_by_id(id)
        results = database.search(query == id)
        
        # Ensure the record exists before proceeding
        if len(results) == 0:
            raise Exception(f"Document is not in the database for id {id}")
        
        result = results[0]
        file_name = result[self._KEY_FILE_NAME]
        
        # Retrieve the content associated with the record using the configured path
        content = None
        with open(self._database_directory + "/" + self._DOCUMENT_DATABASE_CONTENT + "/" + file_name, "r",  encoding='utf-8') as f:
            content = f.read()
        metadata = result[self._KEY_METADATA]
        
        return (metadata, content)

    def insert(self, id: str, metadata: Dict[str, any], content: str) -> None:
        """
        Stores the provided content and metadata, associating them with the 
        given identifier for future retrieval.

        Args:
            id (str): The unique identifier to assign to this document.
            metadata (Dict[str, any]): A dictionary of additional properties associated with the document.
            content (str): The raw text content to be stored.

        Returns:
            None

        Raises:
            Exception: If the provided identifier is already registered in the system.
        """
        # Guard clause to prevent duplicate entries
        if self.has(id):
            raise Exception(f"Document is already in the database for id {id}")
        
        database = self._get_database()
        # Generate a unique internal reference
        file_name = str(uuid4())
        
        # Write the content to the configured storage path
        with open(self._database_directory + "/" + self._DOCUMENT_DATABASE_CONTENT + "/" + file_name, "w", encoding="utf-8") as f:
            f.write(content)
        
        document_record = {}
        document_record[self._KEY_ID] = id
        document_record[self._KEY_FILE_NAME] = file_name

        # Ensure metadata is a dictionary before storage
        stored_metadata = metadata if metadata else {}
        document_record[self._KEY_METADATA] = stored_metadata
            
        database.insert(document_record)
