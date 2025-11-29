import sys
sys.dont_write_bytecode = True

import os
import logging

import asyncio
import platform

from dotenv import load_dotenv

def suppress_useless_logging():
    """
    Suppresses some useless logging.
    """
    logging.getLogger("xhtml2pdf").setLevel(logging.ERROR)
        
def potential_fix_for_event_loops():
    """
    Sets the event loop policy to WindowsSelectorEventLoopPolicy on Windows.
    This prevents 'RuntimeError: Event loop is closed' in most of the cases.
    """
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
def initialize_environment_variables():
    """
    Initializes environment variables for the application.
    """

    # load dotenv and check that the relevant variables are set
    load_dotenv()

    assert not os.environ["GOOGLE_API_KEY"] is None
    assert not os.environ["BASELINE_LLM"] is None

    logging.info(f"Environment variables initialized successfully.")
    logging.info(f"Using baseline model {os.environ["BASELINE_LLM"]}.")

# initialize environment variables
initialize_environment_variables()

# prevent logging noise
suppress_useless_logging()

# fix potential errors with event loops
potential_fix_for_event_loops()

