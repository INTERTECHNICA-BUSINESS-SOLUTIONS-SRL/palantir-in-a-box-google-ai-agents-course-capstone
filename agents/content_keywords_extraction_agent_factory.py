from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory


class ContentKeywordsExtractionAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "keywords"

    def _get_name(self) -> str:
        return "ContentKeywordsExtractionAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in extracting content keywords.
                The keywords extraction rules are specified in the task description.
            </role>
            <task_description>
                You will receive content that needs keywords extraction in the content section. 
                
                You will extract the keywords from the content according to the following rules:
                
                * Use only the information in the content provided, do not include anything else you may additionally know.
                * Avoid keywords overlap.
                * Ensure complete coverage of the critical information.
                * Do not include any links, images, videos or other non-text elements in the keywords.
                
                Return only the keywords extracted as a comma separated string of values, the most relevant keywords being at the beginning.
            </task_description>
            <content>
            {cleaned_up_content}
            </content>
            <format>
                You will return only the keywords extracted as a comma separated string of values.
                Do not add any acknowledgements or introductions.
            </format>         
        """

        return instruction

    def _get_output_key(self):
        return ContentKeywordsExtractionAgentFactory._OUTPUT_KEY

