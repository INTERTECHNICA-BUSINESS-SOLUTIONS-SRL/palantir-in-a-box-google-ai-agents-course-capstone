import logging

from mistletoe import markdown
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa

TEMPLATES_PATH = "./0_0_3_templates"
ACH_REPORT_CONTENT_HTML_WRAPPER_TEMPLATE = "ach_report_content_html_wrapper_template.jinja"

def _generate_report_html_wrapped_content (
    content: str
) -> str:
    """
    Wraps the provided HTML content for processing into PDF format later on.

    Args:
        content (str): The HTML content to be wrapped.

    Returns:
        str: The rendered HTML string containing the wrapped content.
    """
    # loads the report html wrapper template
    environment = Environment(loader=FileSystemLoader(TEMPLATES_PATH))
    template = environment.get_template(ACH_REPORT_CONTENT_HTML_WRAPPER_TEMPLATE)
    
    # render the generated html wrapped content
    html_wrapped_content = template.render(
        content = content,
    )

    return html_wrapped_content

def generate_pdf_from_markdown(
    report_mark_down_content : str,
    file_name: str
) -> None:
    """
    Generates a PDF file from raw Markdown content.

    Args:
        report_mark_down_content (str): The source content in Markdown format.
        file_name (str): The target file path where the PDF will be saved.
    """    
    # get html wrapped content as a basis for PDF content generation
    report_html_content = markdown(report_mark_down_content)
    
    # generate the html wrapped content of the report
    report_html_wrapped_content = _generate_report_html_wrapped_content(report_html_content)
    
    # generated the pdf and write it at the specified location
    with open(file_name, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(report_html_wrapped_content, dest=pdf_file)
        if pisa_status.err:
            logging.error(f"PDF file creation failed with error: {pisa_status.err}")
            raise Exception(f"PDF file creation failed with error: {pisa_status.err}")

    logging.debug(f"PDF file created successfully")