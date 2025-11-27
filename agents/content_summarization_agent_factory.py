from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory


class ContentSummarizationAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "summary"

    
    def _get_name(self) -> str:
        return "ContentSummarizationAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in content summarization.
                The content summarizations rules are specified in the task description.
            </role>
            <task_description>
                You will receive content that needs to be summarized in the content section. 
                
                You will summarize the content according to the following rules:
                
                * Use only the information in the content provided, do not include anything else you may additionally know.
                * Consider the most relevant information.
                * Do not allow repeated information in the summarization.
                * Do not include any links, images, videos or other non-text elements in the summarization.
                * Use bold markup to highlight critical information.
                * The summary must no longer than 3 paragraphs long
                
                Avoid returning the content as a an identical copy of the original content.
                Do not recite the content, avoid RECITATION termination.
                
                Return only the summarized content.
            </task_description>
            <content>
            {cleaned_up_content}
            </content>
            <format>
                You will return only the summarized content as text with markup if needed.
                Do not add any acknowledgements or introductions.
            </format>         
        """

        return instruction
    
    def _get_output_key(self):
        return ContentSummarizationAgentFactory._OUTPUT_KEY