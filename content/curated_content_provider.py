from typing import Dict, Tuple

from pydantic_core import from_json

from content.provider import ContentProvider
from document_database import DocumentDatabase

from agent_runners.simple_runner import SimpleRunner
from agents.workflow_document_content_assembling_agent_factory import WorkflowDocumentInformationAssemblingAgentFactory

class CuratedContentProvider(ContentProvider):
    """
    Concrete implementation of the ContentProvider interface.
    Curates the content after retrieval
    """
    
    _DOCUMENT_STORAGE = "./0_0_2_cache/0_0_2_curated"
    
    def __init__(self):
        """
        Initializes the content provider system.
        """
        super().__init__()
        self._document_database = DocumentDatabase.get_implementation(self._DOCUMENT_STORAGE)
        
    def _run_retrieval_workflow(self, url: str) -> Tuple[Dict[str, any], str] :
        
        runner = SimpleRunner()
        agent = WorkflowDocumentInformationAssemblingAgentFactory().get_agent()
        
        agent_response = runner.run(agent, f"Process the content from {url}")
        document_information  = from_json(agent_response)
        
        metadata = {
            "url": url,
            "title": document_information["title"],
            "authors": document_information["authors"],
            "keywords": document_information["keywords"],
            "summary": document_information["summary"]
        }
        content = document_information["content"]

        return (metadata, content)

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

        metadata, content = self._run_retrieval_workflow(url)
        
        # Store content and metadata for future access
        self._document_database.insert(url, metadata, content)
                    
        return (metadata, content)
