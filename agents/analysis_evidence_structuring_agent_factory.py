from typing import List, Dict
from pydantic import BaseModel, Field
from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory

class AnalysisEvidenceHypothesisSupportItem(BaseModel):
    hypothesis: str = Field(description = "The hypothesis supported")
    support: str = Field(description = "The level of evidence support for the hypothesis")
    reasoning: str = Field(description = "The reasoning for the level of evidence support for the hypothesis")

class AnalysisEvidenceStructuringItem(BaseModel):
    evidence: str = Field(description = "The evidence name")
    description: str = Field(description = "The evidence description")
    relevance: str = Field(description = "The evidence relevance")
    relevance_reasoning: str = Field(description = "The evidence relevance reasoning")
    objectivity: str = Field(description = "The evidence objectivity")
    objectivity_reasoning: str = Field(description = "The evidence objectivity reasoning")
    source: str = Field(description = "The evidence source")
    url: str = Field(description = "The evidence url")
    hypotheses_support: List[AnalysisEvidenceHypothesisSupportItem] = Field(description = "The level of evidence support for these items")

class AnalysisEvidenceStructuringAgentOutput(BaseModel):
    evidence_items: List[AnalysisEvidenceStructuringItem] = Field(description = "The list of extracted evidence items")
    
class AnalysisEvidenceStructuringAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "analysis_evidence_structured"

    def _get_name(self) -> str:
        return "AnalysisEvidenceStructuringAgent"

    def _get_instruction(self) -> str:
        instruction = """
            <role>
                You are an expert agent specialized in structuring the evidence data for further processing.
            </role>
            <task>
                You will receive a list of evidence items in markdown format. 
                For each of the evidence item in the list, you will construct a JSON object with the following fields:
                
                * evidence: the evidence text, usually represented by an Evidence text
                * description: the evidence description, usually represented by a Description field
                * relevance: the evidence relevance, usually represented by a Relevance field
                * relevance_reasoning: the evidence relevance reasoning, usually represented by a RelevanceReasoning field
                * objectivity: the evidence objectivity, usually represented by an Objectivity field
                * objectivity_reasoning: the evidence objectivity reasoning, usually represented by an ObjectivityReasoning field
                * source: the evidence source, usually represented by a Source field
                * url: the evidence url, usually represented by an URL field
                * hypotheses_support: the information of the level of evidence support for hypotheses, usually represented by an Hypotheses Support field. It is a list of objects having the following fields:
                    - hypothesis: the hypothesis, extracted from the Hypotheses Support list item
                    - support: the level of support (), extracted from the Hypotheses Support list item. May be one of "strongly supports" "supports", "irrelevant", "contradicts", "strongly contradicts"
                    - reasoning: the evidence support reason, extracted from the Hypotheses Support list item. It usually follows the evidence support information in the list item.
                
            </task>
            <format>
                Return the extracted evidence items as a JSON object having the following field:
                
                * evidence_items: the list of evidence objects extracted from the evidence data
            </format>       
        """

        return instruction
    
    def _get_additional_arguments(self) -> Dict[str, any]:
        additional_arguments = {
            "output_schema" : AnalysisEvidenceStructuringAgentOutput
        }
        return additional_arguments
    
    def _get_output_key(self):
        return AnalysisEvidenceStructuringAgentFactory._OUTPUT_KEY

