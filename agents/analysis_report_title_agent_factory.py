from agents.base_gemini_llm_agent_factory import BaseGeminiLLMAgentFactory

class AnalysisReportTitleAgentFactory(BaseGeminiLLMAgentFactory):
    _OUTPUT_KEY = "analysis_report_title"

    def _get_name(self) -> str:
        return "AnalysisReportTitleAgent"

    def _get_instruction(self) -> str:
        instruction = """
        <role>
            You are a professional information analyst having an objective perspective and a strong analytical language.
            You are highly proficient in analytical tasks, following them in detail and executing them exactly as specified.
            You will only use the information you were provided, excluding anything else you may think you know.
        </role>
        <task>
            You will generate a document title based on provided data.
            
            You will generate the title based on the following title:
            
            * If the user has provided specific instructions for generating the title, you will follow EXACTLY the instructions provided
            * If no instructions have been provided, generate a generic title based on the data provided
            * If the user has provided a specific format, you will use EXACTLY the format provided 
            
        </task>
        <format>
            The title should be returned as text content.
            Do not add any acknowledgements or introductions.
        </format>
        """

        return instruction
    
    def _get_output_key(self):
        return AnalysisReportTitleAgentFactory._OUTPUT_KEY

