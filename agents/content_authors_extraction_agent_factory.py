from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory


class ContentAuthorsExtractionAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "authors"

    def _get_name(self) -> str:
        return "ContentAuthorsExtractionAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in extracting document authors from their content.
                The author extraction rules are specified in the task description.
            </role>
            <task_description>
                You will receive content that needs authors extraction in the content section. 
                
                You will extract the authors from the content according to the following rules:
                
                * Use only the information in the content provided, do not include anything else you may additionally know.
                * Extract the authors from the document's content. The authors MUST be clearly and explicitly specified in the content. 
                * The authors must be explicitly specified as being authors in content, do not just use any mentioned person.
                * The authors must be extracted from the content, do not generate them.
                * If you cannot identify any author, use an empty value.
                
                Return only the authors extracted as a comma separated string of values.
                If no authors are explicitly identified or mentioned use an empty value.
            </task_description>
            <content>
            {original_content}
            </content>
            <format>
                You will return only the authors extracted as a comma separated string of values.
                If no authors are explicitly identified or mentioned use an empty value.
                Do not add any acknowledgements or introductions.
            </format>         
        """

        return instruction

    def _get_output_key(self):
        return ContentAuthorsExtractionAgentFactory._OUTPUT_KEY

