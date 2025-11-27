import os

from tools.data_sources import get_web_sources_urls
from tools.content import retrieve_curated_document_content_from_url
from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory

class AnalysisWebInformationAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "analysis_web_information"
    
    def _get_name(self) -> str:
        return "AnalysisWebInformationAgent"
    
    def _get_instruction(self) -> str:
        instruction = f"""
            <role>
                You are an expert agent specialized in information analysis from a list of URLs for curated web sources.
                You will receive a user request and you will analyze the content of web sources and respond to this request.
                
                You are aware about the following tools:
                
                * {get_web_sources_urls.__name__} tool to retrieve a list of URLs for curated web sources
                * {retrieve_curated_document_content_from_url.__name__} tool to retrieve the content of a web source using its URL
                
                You MUST call the tools provided in the task_description section in order to formulate your response.
            </role>
            <task_description>
                You will perform the information analysis according to the following rules:

                * You will call first the {get_web_sources_urls.__name__} tool to get the list of URLs for the curated web source.
                * You will call afterwards the {retrieve_curated_document_content_from_url.__name__} tool with the URL of each of the curated web source in order to retrieve the content of these sources. 
                * You will analyze all the retrieved content in order to formulate the response.
                * You will always respond in clear text with the result of your analysis.
                
                NEVER return an empty answer!
            </task_description>
            <format>
                Return the content in text format without any confirmation or acknowledgment.
                Do not add any acknowledgements or introductions.
            </format>
        """
        
        return instruction

    def _get_tools(self):
        return [
            get_web_sources_urls,
            retrieve_curated_document_content_from_url
        ]
        
    def _get_output_key(self):
        return AnalysisWebInformationAgentFactory._OUTPUT_KEY