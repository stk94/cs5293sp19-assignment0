import json
import random
import urllib.request

# Python3 type hints
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
from typing import List, Dict, Any

url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"


def download():
    """ This function downloads the json data from the url."""
    response = urllib.request.urlopen(url)
    text = response.read()      # a `bytes` object
    data = text.decode('utf-8') # a `str`; this step can't be used if data is binary
    extract_requests(data)
    return data


def extract_requests(text: str) -> List[Dict[str, Any]]:
    """
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """
    data_load = json.loads(text)
    promises = data_load['promises']
    extract_titles(promises)
    return promises


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """
    title = []
    for count in promises:
        title.append(count['title'])
    random_title(title)
    return title


def random_title (titles: List[str]) -> str:
    """ This function takes list of titles and returns one string at random. """
    length = len(titles)
    choice = random.randint(0,length)
    return titles[choice]




