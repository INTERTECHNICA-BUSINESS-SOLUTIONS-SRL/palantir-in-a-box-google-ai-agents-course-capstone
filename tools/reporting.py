import json
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader

TEMPLATES_PATH = "./0_0_3_templates"
ACH_REPORT_TEMPLATE = "ach_report_markdown_template.jinja"

def generate_report_markdown_content (
            report_title: str,
            user_request_data: str,
            hypotheses_data: Dict[str, Any], 
            executive_review_data: str,
            actionable_information_data: str,
            evidence_analysis_data: str
        ) -> str:

    # loads the report template
    environment = Environment(loader=FileSystemLoader(TEMPLATES_PATH))
    template = environment.get_template(ACH_REPORT_TEMPLATE)

    # format user request for block quotes
    user_request_block_quotes = user_request_data.replace("/n", "/n >")
    
    # this is a structured JSON string,
    # load it as a JSON object for future processing
    hypotheses_json_data = json.loads(hypotheses_data)
    hypotheses_list = "\t * " + "\n \t * ".join(hypotheses_json_data["hypotheses"])
    hypotheses_reasoning = hypotheses_json_data["reasoning"]
    
    # render the generated report
    report_content = template.render(
        report_title = report_title,
        user_request_data = user_request_block_quotes,
        hypotheses_list = hypotheses_list,
        hypotheses_reasoning = hypotheses_reasoning,
        executive_review_data = executive_review_data,
        actionable_information_data = actionable_information_data,
        evidence_analysis_data = evidence_analysis_data
    )

    return report_content
