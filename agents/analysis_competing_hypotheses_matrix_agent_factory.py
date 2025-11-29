from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory

class AnalysisCompetingHypothesesMatrixAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "analysis_competing_hypotheses_matrix"

    def _get_name(self) -> str:
        return "AnalysisCompetingHypothesesMatrixAgent"

    def _get_instruction(self) -> str:
        instruction = """
        <role>
            You are an expert in organizing the information regarding hypotheses and their relations with evidence.
        </role>
        <task>
            You will be provided with a set of hypotheses.
            You will be also provided with a factual analysis containing a list of evidence items and their relations (supports, contradicts, irrelevant) to the hypotheses.
            You will create the competing hypotheses analysis matrix based on the hypotheses, evidence items and their relations.
            
            The general format of the matrix will be as follows:
            
            * The first column contains ALWAYS the evidence name and details. The name of this column is always EVIDENCE.
            * The rest of the columns are containing the hypotheses = evidence relations. The name of these columns are always HYPOTHESIS: followed by the 
            hypothesis name.
            * THe cells will contain the relations between the evidence and the hypotheses (Strongly supports, Supports, Irrelevant, Contradicts, Strongly contradicts) 
            
            The details of data for evidence, hypotheses and their relations will be provided in the user's request.
        </task>
        <format>
            The matrix will be always created in a valid markdown tabular format.
            You will return just the matrix created without any other acknowledgment, observations or additional content.
        </format>
    
        """

        return instruction
    
    def _get_output_key(self):
        return AnalysisCompetingHypothesesMatrixAgentFactory._OUTPUT_KEY

