import sys
sys.dont_write_bytecode = True

import os
import logging

from dotenv import load_dotenv

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
