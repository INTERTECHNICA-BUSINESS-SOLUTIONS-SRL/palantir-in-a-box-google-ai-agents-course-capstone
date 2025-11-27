from typing import Dict

from pydantic import BaseModel, Field
from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory

class DocumentInformationOutput(BaseModel):
    title: str = Field(description = "The title extracted from the the document's content")
    authors: str = Field(description = "The authors extracted from the the document's content")
    keywords: str = Field(description = "The keywords extracted from the the document's content")
    summary: str = Field(description = "The summary of the document's content")
    content: str = Field(description = "The content of the document, usually cleaned up")

class DocumentInformationAssemblingAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "assembled_document"
    
    def _get_name(self) -> str:
        return "ContentDocumentAssemblingAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in content assembling document's content using different content parts.
                The document's content assembling rules are specified in the task description.
            </role>
            <task_description>
                You will receive content parts that needs to be assembled in a JSON object having the following properties: 
                
                * title - the title of the document present in the title_data section
                * authors - the authors of the document present in the authors_data section
                * summary - the summarized content present in the summary_data section 
                * keywords - the keywords extracted from content, present in the keywords_data section 
                * content - the cleaned up content present in the cleaned_up_content_data section.
                
                Return only the JSON object using JSON format.
            </task_description>
            <title_data>
            {title}
            </title_data>
            <authors_data>
            {authors}
            </authors_data>
            <keywords_data>
            {keywords}
            </keywords_data>
            <summary_data>
            {summary}
            </summary_data>
            <cleaned_up_content_data>
            {cleaned_up_content}
            </cleaned_up_content_data>
            <format>
                You will return only the JSON object constructed according to the rules.
                Do not add any acknowledgements or introductions.
            </format>         
        """

        return instruction
    
    def _get_additional_arguments(self) -> Dict[str, any]:
        additional_arguments = {
            "output_schema" : DocumentInformationOutput
        }
        return additional_arguments

    def _get_output_key(self):
        return DocumentInformationAssemblingAgentFactory._OUTPUT_KEY
    