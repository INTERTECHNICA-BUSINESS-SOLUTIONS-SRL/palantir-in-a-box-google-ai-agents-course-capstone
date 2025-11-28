from tools.prompting import generate_evidence_extraction_prompt
from tools.prompting import generate_evidence_structuring_prompt
from tools.prompting import generate_evidence_in_depth_analysis_prompt
from tools.prompting import generate_evidence_analysis_executive_review_prompt
from tools.prompting import generate_actionable_information_prompt
from tools.prompting import generate_report_title_prompt

from tools.reporting import generate_report_content

from agents.analysis_hypotheses_extraction_agent_factory import AnalysisHypothesesExtractionAgentFactory
from agents.analysis_web_information_agent_factory import AnalysisWebInformationAgentFactory
from agents.analysis_evidence_structuring_agent_factory import AnalysisEvidenceStructuringAgentFactory
from agents.analysis_evidence_detailed_analysis_agent_factory import AnalysisEvidenceDetailedAnalysisAgentFactory
from agents.analysis_executive_review_agent_factory import AnalysisExecutiveReviewAgentFactory
from agents.analysis_actionable_information_agent_factory import AnalysisActionableInformationAgentFactory
from agents.analysis_report_title_agent_factory import AnalysisReportTitleAgentFactory

from agent_runners.simple_runner import SimpleRunner

def run_workflow_analysis_of_competing_hypotheses(user_request: str) -> str:
    
    # first extract the hypotheses
    runner = SimpleRunner()
    extracted_hypotheses = runner.run(
        AnalysisHypothesesExtractionAgentFactory().get_agent(),
        user_request
    )
    
    # extract the evidence from the data
    extracted_evidence = runner.run(
        AnalysisWebInformationAgentFactory().get_agent(),
        generate_evidence_extraction_prompt(extracted_hypotheses)
    )

    # structure the extracted evidence 
    structured_evidence = runner.run(
        AnalysisEvidenceStructuringAgentFactory().get_agent(),
        generate_evidence_structuring_prompt(extracted_evidence)
    )

    # perform an in depth analysis of the structured evidence and its support for hypotheses 
    detailed_evidence_analysis = runner.run(
        AnalysisEvidenceDetailedAnalysisAgentFactory().get_agent(),
        generate_evidence_in_depth_analysis_prompt(extracted_hypotheses, structured_evidence)
    )

    # generate the executive review 
    executive_review = runner.run(
        AnalysisExecutiveReviewAgentFactory().get_agent(),
        generate_evidence_analysis_executive_review_prompt(extracted_hypotheses, detailed_evidence_analysis)
    )
    
    # generate the actionable information 
    actionable_information = runner.run(
        AnalysisActionableInformationAgentFactory().get_agent(),
        generate_actionable_information_prompt(
            user_request, 
            extracted_hypotheses,
            detailed_evidence_analysis,
            executive_review
        )
    )
    
    # generate the report title 
    report_title = runner.run(
        AnalysisReportTitleAgentFactory().get_agent(),
        generate_report_title_prompt(
            user_request, 
            extracted_hypotheses,
            executive_review
        )
    )
    
    # assemble the report content
    report_content = generate_report_content (
        report_title = report_title,
        user_request_data = user_request,
        hypotheses_data = extracted_hypotheses,
        executive_review_data = executive_review,
        actionable_information_data = actionable_information,
        evidence_analysis_data = detailed_evidence_analysis
    )
    
    return report_content