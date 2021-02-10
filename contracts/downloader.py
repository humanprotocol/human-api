import os
import requests
import logging
import json
from urllib.parse import urlparse
from multiprocessing.pool import ThreadPool

LOGGER = logging.getLogger("Contracts:Downloader")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.split(parsed_url.path)[1]
    return filename


def download_file(url):
    filename = get_filename_from_url(url)
    data = ""
    LOGGER.info("Downloading %s", filename)
    response = requests.get(url)
    if response.status_code ==  200:
        LOGGER.info("Successfully Downloaded %s", filename)
        data = response.text
    else:
        LOGGER.error("Error Downloading %s", filename)
    return {"filename": filename, "content": data}

    
def download_multiple_files(urls):
    results = ThreadPool(5).map(download_file, urls)
    return results