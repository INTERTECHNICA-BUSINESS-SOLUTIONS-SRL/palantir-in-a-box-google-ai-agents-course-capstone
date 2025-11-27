from google.adk.agents import Agent, SequentialAgent

from agents.content_retrieval_agent_factory import ContentRetrievalAgentFactory
from agents.content_title_extraction_agent_factory import ContentTitleExtractionAgentFactory
from agents.content_authors_extraction_agent_factory import ContentAuthorsExtractionAgentFactory
from agents.content_cleanup_agent_factory import ContentCleanupAgentFactory
from agents.content_summarization_agent_factory import ContentSummarizationAgentFactory
from agents.content_keywords_extraction_agent_factory import ContentKeywordsExtractionAgentFactory
from agents.document_information_assembling_agent_factory import DocumentInformationAssemblingAgentFactory

class WorkflowDocumentInformationAssemblingAgentFactory:
    def __init__(self):
        self.content_retrieval_agent_factory = ContentRetrievalAgentFactory()
        self.content_title_extraction_agent_factory = ContentTitleExtractionAgentFactory()
        self.content_authors_extraction_agent_factory = ContentAuthorsExtractionAgentFactory()
        self.content_cleanup_agent_factory = ContentCleanupAgentFactory()
        self.content_summarization_agent_factory = ContentSummarizationAgentFactory()
        self.content_keywords_extraction_agent_factory = ContentKeywordsExtractionAgentFactory()
        self.document_information_assembling_agent_factory = DocumentInformationAssemblingAgentFactory()

    def _get_name(self) -> str:
        return "WorkflowDocumentInformationAssemblingAgent"

    def get_agent(self) -> Agent:
        agent = SequentialAgent(
            name = self._get_name(),
            sub_agents = [
                self.content_retrieval_agent_factory.get_agent(), 
                self.content_title_extraction_agent_factory.get_agent(), 
                self.content_authors_extraction_agent_factory.get_agent(), 
                self.content_cleanup_agent_factory.get_agent(),
                self.content_summarization_agent_factory.get_agent(),
                self.content_keywords_extraction_agent_factory.get_agent(),
                self.document_information_assembling_agent_factory.get_agent()
            ]
        )
        
        return agent