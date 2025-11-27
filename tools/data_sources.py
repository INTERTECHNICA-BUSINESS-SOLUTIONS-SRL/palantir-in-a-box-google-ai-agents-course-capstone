import logging
import pandas as pd

from typing import List

# define the file path to the csv containing the registry of approved web sources
_WEB_SOURCES_PATH = "0_0_1_data_sources/web_sources.csv"

def get_web_sources_urls() -> List[str]:
    """
    Gets a list of URLs which represent curated articles from web used for analysis. 
    When analyzing data from the web, select data only from this list. Do not attempt to search the web for data. 
    This can be used as a tool. 

    Returns:
        List[str]: The list of URLs for curated web data.
    """
    # log the initiation of the tool for debugging and tracing purposes
    logging.debug(f"Get curated articles web links tool is called")

    # load the approved sources from the configured csv file
    curated_articles_data_frame = pd.read_csv(_WEB_SOURCES_PATH, header=0, sep=",", encoding="utf-8")

    # extract the specific column containing urls and convert it to a standard list
    articles_links = curated_articles_data_frame["web_sources"].values.tolist()

    # log the results before returning to verify the output
    logging.debug(f"Returning the list of curated articles: {articles_links}")
    
    return articles_links