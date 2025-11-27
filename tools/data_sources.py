import logging
import pandas as pd

from typing import List

_WEB_SOURCES_PATH = "0_0_1_data_sources\web_sources.csv"

def get_web_sources_links() -> List[str]:
    """
    Gets a list of URLs which represent curated articles from web used for analysis. 
    When analyzing data from the web, select data only from this list. Do not attempt to search the web for data. 
    This can be used as a tool. 

    Returns:
        The list of URLs for curated web data.
    """
    logging.debug(f"Get curated articles web links tool is called")

    curated_articles_data_frame = pd.read_csv(_WEB_SOURCES_PATH, header=0, sep=",", encoding="utf-8")
    articles_links = curated_articles_data_frame["articles"].values.tolist()

    logging.debug(f"Returning the list of curated articles: {articles_links}")
    
    return articles_links
