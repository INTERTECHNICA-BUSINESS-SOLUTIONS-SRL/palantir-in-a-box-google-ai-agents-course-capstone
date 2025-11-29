from typing import List, Dict
from pydantic import BaseModel, Field
from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory

class AnalysisHypothesesExtractionAgentOutput(BaseModel):
    hypotheses: List[str] = Field(description= "The list of hypotheses")
    reasoning: str = Field(description= "The reasoning for hypotheses extraction")    
    
class AnalysisHypothesesExtractionAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "analysis_hypotheses_extracted"

    def _get_name(self) -> str:
        return "AnalysisHypothesesExtractionAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in hypotheses extraction from an analyst request stated in natural language.
            </role>
            <task>
                You will extract the hypotheses from the analyst request section according to the following rules:
                
                * Extract the hypotheses in a clear and concise manner. Brevity and clarity are absolutely necessary here   .
                * Make sure that the hypotheses are well-formed and logically sound.
                * Make sure that the hypotheses do not overlap with each other.

                There is a possibility that no hypotheses can be extracted from the provided text, make sure to handle this case as specified in the format section.
            </task>
            <format>
                Return the extracted hypotheses as a JSON object with the following fields:
                
                hypotheses: the list of strings representing the extracted hypotheses.
                reasoning: a string, the explanation of why you have formulated these hypotheses. Formulate this in an analytical language using a single sentence.
            </format>       
        """

        return instruction
    
    def _get_additional_arguments(self) -> Dict[str, any]:
        additional_arguments = {
            "output_schema" : AnalysisHypothesesExtractionAgentOutput
        }
        return additional_arguments
    
    def _get_output_key(self):
        return AnalysisHypothesesExtractionAgentFactory._OUTPUT_KEY

