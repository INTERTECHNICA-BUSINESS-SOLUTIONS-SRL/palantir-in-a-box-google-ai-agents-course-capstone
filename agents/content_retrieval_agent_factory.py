import os

from tools.content import retrieve_content_from_url
from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory

class ContentRetrievalAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "original_content"
    
    def _get_name(self) -> str:
        return "ContentRetrievalAgent"
    
    def _get_baseline_llm(self) -> str:
        assert not os.environ["BASELINE_LLM"] is None
        return os.environ["BASELINE_LLM"]
    
    def _get_instruction(self) -> str:
        instruction = f"""
            <role>
                You are an expert agent specialized in content retrieval operations using URL addresses by using the '{retrieve_content_from_url.__name__}'. 
                THis tool which must ALWAYS be called in the process of content retrieval. Never provide your own information.
                The content retrieval procedure is described in the task description and you MUST call the tool provided in the task_description.
            </role>
            <task_description>
                You will receive a web URL from which you will have to retrieve the content using the following rules:
                
                1. You MUST ALWAYS call the '{retrieve_content_from_url.__name__}' tool to retrieve the content from the URL.
                Respond with the content returned by the '{retrieve_content_from_url.__name__}' tool without any changes or modifications.
                2. You MUST ALWAYS reply with the content exactly as returned by the tool. No modifications to it!

                IMPORTANT: Never return an empty answer.
            </task_description>
            <format>
                Return the content in text format without any confirmation or acknowledgment.
                Do not modify the content under any circumstances.
                Do not add any acknowledgements or introductions.
            </format>
        """
        
        return instruction

    def _get_tools(self):
        return [
            retrieve_content_from_url
        ]
        
    def _get_output_key(self):
        return ContentRetrievalAgentFactory._OUTPUT_KEY