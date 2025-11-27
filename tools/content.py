from typing import Tuple, Dict, Any
from markdownify import markdownify

def retrieve_metadata_and_content_from_url(url: str) -> Tuple[Dict[str, Any], str]:
    """
    Fetches a webpage and returns its metadata together with the main content converted to Markdown.

    Args:
        url (str): The URL to retrieve.

    Returns:
        Tuple[Dict[str, Any], str]: 
            - Dictionary containing page metadata (title, description, etc.)
            - Page content converted to Markdown (ATX-style headings)
    """
    from content.web_content_provider import WebContentProvider

    web_content_provider = WebContentProvider()
    # retrieve raw HTML and extracted metadata from the webpage
    metadata, content = web_content_provider.retrieve(url)
    # convert the retrieved HTML content to clean Markdown using ATX-style headings
    markdownified_content = markdownify(content, heading_style="ATX")
    
    return metadata, markdownified_content


def retrieve_content_from_url(url: str) -> str:
    """
    Retrieves the content from a URL as clean Markdown.

    Args:
        url (str): The URL to retrieve content from.

    Returns:
        str: Webpage content in Markdown format.
    """
    # call the full retrieval function but keep only the Markdown content
    _, content = retrieve_metadata_and_content_from_url(url)
    return content


def retrieve_curated_metadata_and_content_from_url(url: str) -> Tuple[Dict[str, Any], str]:
    """
    Retrieves metadata and cleaned content from a curated source.

    Args:
        url (str): The URL of the curated page.

    Returns:
        Tuple[Dict[str, Any], str]:
            - Dictionary with page metadata
            - Cleaned text content (typically already structured)
    """
    from content.curated_content_provider import CuratedContentProvider

    curated_content_provider = CuratedContentProvider()
    
    # curated sources provide pre-cleaned content and structured metadata
    metadata, content = curated_content_provider.retrieve(url)
    
    return metadata, content


def retrieve_curated_content_from_url(url: str) -> str:
    """
    Retrieves cleaned content from a curated source (metadata is discarded).

    Args:
        url (str): The URL to retrieve curated content from.

    Returns:
        str: Cleaned text content from the source.
    """
    # use the metadata-aware version but return only the cleaned content
    _, content = retrieve_curated_metadata_and_content_from_url(url)
    return content

def retrieve_curated_document_content_from_url(url: str) -> str:
    """
    Retrieves a curated page and returns a fully formatted, self-contained Markdown document.

    The output includes title, source URL, keywords, and a blockquote-formatted summary,
    followed by a separator and the full cleaned content — ideal for archiving or feeding to LLMs.

    Args:
        url (str): The URL of the curated document.

    Returns:
        str: Complete Markdown document with header information and content.
    """
    # fetch both metadata and cleaned content from the curated source
    metadata, content = retrieve_curated_metadata_and_content_from_url(url)
    
    # extract key fields for the document header
    title = metadata["title"]
    keywords = metadata["keywords"]
    summary = metadata["summary"]

    # assemble the final document with clear sections and visual separation
    document_content = f"""
# {title}

**URL**: [{url}]({url})

**Keywords**: {keywords}

**Summary**:

{"> " + summary.replace("\n", "\n>")}

---
    
{content}    
"""

    # return the complete document (leading/trailing newlines are intentional for clean rendering)
    return document_content.strip() + "\n"