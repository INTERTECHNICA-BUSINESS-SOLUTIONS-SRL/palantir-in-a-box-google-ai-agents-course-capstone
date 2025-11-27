from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory


class ContentTitleExtractionAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "title"

    def _get_name(self) -> str:
        return "ContentTitleExtractionAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in extracting document titles from their content.
                The title extraction rules are specified in the task description.
            </role>
            <task_description>
                You will receive content that needs title extraction in the content section. 
                
                You will extract the title from the content according to the following rules:
                
                * Use only the information in the content provided, do not include anything else you may additionally know.
                * Extract the most likely title from the document's content.
                * The title must be extracted from the document's content, do not generate it.
                * If you cannot extract any title, return the value UNTITLED.
                
                Return only the title extracted.
            </task_description>
            <content>
            {original_content}
            </content>
            <format>
                You will return only the title extracted as text.
                Do not add any acknowledgements or introductions.
            </format>         
        """

        return instruction

    def _get_output_key(self):
        return ContentTitleExtractionAgentFactory._OUTPUT_KEY

