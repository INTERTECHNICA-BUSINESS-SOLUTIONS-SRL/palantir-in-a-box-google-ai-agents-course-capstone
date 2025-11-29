from tools.prompting import generate_evidence_extraction_prompt
from tools.prompting import generate_evidence_structuring_prompt
from tools.prompting import generate_competing_hypotheses_matrix_prompt
from tools.prompting import generate_evidence_in_depth_analysis_prompt
from tools.prompting import generate_evidence_analysis_executive_review_prompt
from tools.prompting import generate_actionable_information_prompt
from tools.prompting import generate_report_title_prompt

from agents.analysis_hypotheses_extraction_agent_factory import AnalysisHypothesesExtractionAgentFactory
from agents.analysis_web_information_agent_factory import AnalysisWebInformationAgentFactory
from agents.analysis_evidence_structuring_agent_factory import AnalysisEvidenceStructuringAgentFactory
from agents.analysis_evidence_detailed_analysis_agent_factory import AnalysisEvidenceDetailedAnalysisAgentFactory
from agents.analysis_competing_hypotheses_matrix_agent_factory import AnalysisCompetingHypothesesMatrixAgentFactory
from agents.analysis_executive_review_agent_factory import AnalysisExecutiveReviewAgentFactory
from agents.analysis_actionable_information_agent_factory import AnalysisActionableInformationAgentFactory
from agents.analysis_report_title_agent_factory import AnalysisReportTitleAgentFactory

from agent_runners.simple_runner import SimpleRunner

# a temporary hack to prevent frequent warnings about
# improper closing of event loops
# the error is usually benign, we've decided for a band aid for now. 
from functools import wraps
def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

@silence_event_loop_closed
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

    # generate the competitive hypotheses matrix
    competing_hypotheses_matrix = runner.run(
        AnalysisCompetingHypothesesMatrixAgentFactory().get_agent(),
        generate_competing_hypotheses_matrix_prompt(extracted_hypotheses, structured_evidence)
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
    
    # assemble the execution results
    execution_result = dict(
        report_title = report_title,
        user_request_data = user_request,
        hypotheses_data = extracted_hypotheses,
        executive_review_data = executive_review,
        actionable_information_data = actionable_information,
        evidence_analysis_data = detailed_evidence_analysis,
        competing_hypotheses_matrix = competing_hypotheses_matrix
    )
    
    # assemble the execution debug data
    # for debugging, auditability and further evaluation
    execution_debug_data = dict(
        extracted_evidence = extracted_evidence,
        structured_evidence = structured_evidence
    )
    
    return execution_result, execution_debug_data