""" This folder can expand to include multuple modules that will have common functionality.
Common functions can be grouped in utils.py until there is a need to separate them."""
from lxml import etree
import io
import requests, bs4
from PIL import Image
from isbnlib import to_isbn13
import json


def get_image_from_url(url):
    """
    Will get the pillow image from a url

        Args:
            url: the URL for the image

        Returns:
            A Pillow image
    """
    if 'http' in url:
        image_response = requests.get(url)
        image_content = io.BytesIO(image_response.content)
    else:
        image_content = "test/scribd/test_pages/the_hunger_games_by_suzanne_collins_files/1585192037"

    img = Image.open(image_content)
    return img

def get_root_from_url(url):
    """
    Will get the lxml root for an html file.

        Args:
            url: the URL for the website

        Returns:
            An etree root for the page.
    """
    if 'http' in url:
        content = io.BytesIO(requests.get(url).content)
    else:
        content = url

    parser = etree.HTMLParser()
    tree = etree.parse(content, parser)
    return tree.getroot()

def get_soup_from_url(url):

    # The following code gets a json blob from inside a specific javascript function call.  
    if 'http' in url:
        res = requests.get(url)
        res.raise_for_status()
        content = res.text
    else: 
        content = open(url, encoding="utf8")

    return bs4.BeautifulSoup(content, "html.parser")

def get_json_from_url(url):
    if 'http' in url:
            api_response = requests.get(url)
            content = api_response.json()

    else:
        content = json.load(open(url, encoding="utf8"))
    return content

def query_html(root, expr, get_first=False):
    """
    Wrapper for node.xpath() to prevent IndexOutOfBounds Exception

        Args:
            root: the starting node for the xpath expression
            expr: the string expression to query with

        Returns:
            - Single node for unique query
            - Array for queries that are not unique
            - None when the query result is empty
    """
    try:
        result = root.xpath(expr)
        if len(result) == 0:
            result = None
        elif len(result) == 1 or get_first:
            result = result[0]

    except:
        print("WARNING: Could not retrieve data for " + expr)

    return result

