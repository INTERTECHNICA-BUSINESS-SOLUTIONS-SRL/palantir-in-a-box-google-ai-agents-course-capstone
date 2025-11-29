import datetime
import json
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader

from tools.library.filenames import get_absolute_path, generate_unique_filename, generate_not_existing_filename
from tools.pdf import generate_pdf_from_markdown

IMAGE_REPORT_PATH = "./0_0_3_templates/resources/agentic_ai_analyst.png"

TEMPLATES_PATH = "./0_0_3_templates"
ACH_REPORT_CONTENT_MARKDOWN_TEMPLATE = "ach_report_markdown_template.jinja"
REPORTS_PATH = "./0_0_4_reports"

def generate_report_markdown_content (
    report_title: str,
    user_request_data: str,
    hypotheses_data: str, 
    executive_review_data: str,
    actionable_information_data: str,
    evidence_analysis_data: str
) -> str:
    """
    Generates the final report content in Markdown format by populating a template from various data information items.

    Args:
        report_title (str): The title of the report.
        user_request_data (str): The original user query or request.
        hypotheses_data (str): A JSON string containing hypotheses and reasoning.
        executive_review_data (str): The executive summary text.
        actionable_information_data (str): The actionable insights text.
        evidence_analysis_data (str): The evidence analysis text.

    Returns:
        str: The fully rendered Markdown report.
    """
    # loads the report template
    environment = Environment(loader=FileSystemLoader(TEMPLATES_PATH))
    template = environment.get_template(ACH_REPORT_CONTENT_MARKDOWN_TEMPLATE)

    # report version and branding
    system_name = "GENESIS ZERO"
    report_version = "==== HAYAWAZA ===="
    generation_date = datetime.datetime.now().strftime("%B %d, %Y")

    # format user request for block quotes
    user_request_block_quotes = "\n >" + user_request_data.replace("\n", "\n >")
    
    # this is a structured JSON string,
    # load it as a JSON object for future processing
    hypotheses_json_data = json.loads(hypotheses_data)
    hypotheses_list = "\t* " + "\n\t* ".join(hypotheses_json_data["hypotheses"])
    hypotheses_reasoning = hypotheses_json_data["reasoning"]
    
    # render the generated report
    report_content = template.render(
        system_name = system_name,
        report_version = report_version,
        generation_date = generation_date,
        report_image_path  = get_absolute_path(IMAGE_REPORT_PATH),
        report_title = report_title,
        user_request_data = user_request_block_quotes,
        hypotheses_list = hypotheses_list,
        hypotheses_reasoning = hypotheses_reasoning,
        executive_review_data = executive_review_data,
        actionable_information_data = actionable_information_data,
        evidence_analysis_data = evidence_analysis_data
    )

    return report_content


def generate_pdf_report_from_markdown_content(
    markdown_content: str,
    report_title: str
) -> str :
    """
    Generates a PDF report from Markdown content, ensuring a unique filename.

    Args:
        markdown_content (str): The content of the report in Markdown format.
        report_title (str): The title used to derive the filename.

    Returns:
        str: The file path of the generated PDF report.
    """
    # retrieve an available filename for the report
    report_file_name = generate_unique_filename(report_title, ".pdf")
    report_file_name = REPORTS_PATH + "/" + report_file_name
    report_file_name = generate_not_existing_filename(report_file_name)
    
    # generate the report
    generate_pdf_from_markdown(
        markdown_content,
        report_file_name
    )
    
    return report_file_name


def generate_report_from_execution_result (
    report_title: str,
    user_request_data: str,
    hypotheses_data: str,
    executive_review_data: str,
    actionable_information_data: str,
    evidence_analysis_data: str
) -> str:
    """
    Orchestrates the creation of a PDF report based on execution results.

    This function generates the report content in Markdown format using the provided
    data and subsequently converts it into a PDF file.

    Args:
        report_title (str): The title of the report.
        user_request_data (str): The original user query or request.
        hypotheses_data (str): A JSON formatted string containing hypotheses and reasoning.
        executive_review_data (str): The executive summary text.
        actionable_information_data (str): The actionable insights text.
        evidence_analysis_data (str): The detailed evidence analysis text.

    Returns:
        str: The file path of the generated PDF report.
    """    
    markdown_content = generate_report_markdown_content(
        report_title,
        user_request_data,
        hypotheses_data,
        executive_review_data,
        actionable_information_data,
        evidence_analysis_data
    )
    
    report_file_path = generate_pdf_report_from_markdown_content(
        markdown_content,
        report_title
    )
    
    return report_file_path