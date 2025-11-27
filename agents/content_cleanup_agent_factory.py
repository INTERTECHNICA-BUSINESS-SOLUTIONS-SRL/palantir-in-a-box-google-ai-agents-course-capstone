from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory


class ContentCleanupAgentFactory(BaseGeminiLLMAgentFactory):
    OUTPUT_KEY = "cleaned_up_content"

    def _get_name(self) -> str:
        return "ContentCleanupAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in web content cleanup.
                The content cleanup rules are specified in the task description.
            </role>
            <task_description>
                You will receive content that needs to be cleaned up in the original_content section. 
                
                You will clean up the content according to the following rules:
                
                * Remove the article title.
                * Remove the article authors.
                * Remove links to other pages.
                * Remove images and videos, including links to them.
                * Remove navigation, side bars and notification boxes.
                * Remove any advertisements, pop-ups and other distracting elements.
                * Remove any other unnecessary elements that do not contribute to the main content.
                
                Use strictly the content you received.
                The content elements you keep should be identical to the original content elements.
                Do not summarize, rephrase or add any other additional information to the content. 
                Avoid returning the content as a an identical copy of the original content.
                Do not recite the content, avoid RECITATION termination.
                
                Return only the cleaned-up content.
            </task_description>
            <original_content>
            {original_content}
            </original_content>
            <format>
                You will return only the cleaned up content as text.
                Do not add any acknowledgements or introductions.
            </format>         
        """

        return instruction

    def _get_tools(self):
        return []

    def _get_output_key(self):
        return ContentCleanupAgentFactory.OUTPUT_KEY