from tools.prompting import generate_evidence_extraction_prompt
from tools.prompting import generate_evidence_structuring_prompt
from tools.prompting import generate_evidence_in_depth_analysis_prompt

from agents.analysis_hypotheses_extraction_agent_factory import AnalysisHypothesesExtractionAgentFactory
from agents.analysis_web_information_agent_factory import AnalysisWebInformationAgentFactory
from agents.analysis_evidence_structuring_agent_factory import AnalysisEvidenceStructuringAgentFactory
from agents.analysis_evidence_detailed_analysis_agent_factory import AnalysisEvidenceDetailedAnalysisAgentFactory

from agent_runners.simple_runner import SimpleRunner

def run_workflow_analysis_of_competing_hypotheses(user_request: str) -> str:
    
    # first extract the hypotheses
    runner = SimpleRunner()
    extracted_hypotheses = runner.run(
        AnalysisHypothesesExtractionAgentFactory().get_agent(),
        user_request
    )
    print(extracted_hypotheses)
    
    # extract the evidence from the data
    runner = SimpleRunner()
    extracted_evidence = runner.run(
        AnalysisWebInformationAgentFactory().get_agent(),
        generate_evidence_extraction_prompt(extracted_hypotheses)
    )
    print(extracted_evidence)

    # structure the extracted evidence 
    runner = SimpleRunner()
    structured_evidence = runner.run(
        AnalysisEvidenceStructuringAgentFactory().get_agent(),
        generate_evidence_structuring_prompt(extracted_evidence)
    )
    print(structured_evidence)

    # perform an in depth analysis of the structured evidence and its support for hypotheses 
    runner = SimpleRunner()
    in_depth_evidence_analysis = runner.run(
        AnalysisEvidenceDetailedAnalysisAgentFactory().get_agent(),
        generate_evidence_in_depth_analysis_prompt(extracted_hypotheses, structured_evidence)
    )
    
    return in_depth_evidence_analysis