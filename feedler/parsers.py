from io import BytesIO

import requests
from defusedxml.ElementTree import parse

from feedler.constants import FeedTypes
from feedler.utils import convert_rss_feed_to_dict, convert_rss_feed_to_json


def _parser(file: str, type=FeedTypes.rss, format=None):
    xml = file

    if "http" in file:
        response = requests.get(file)
        xml = BytesIO(response.content)

    rss = parse(xml)

    if format == "json":
        return convert_rss_feed_to_json(rss)
    return convert_rss_feed_to_dict(rss)


def rss_parser(xmlfile):
    return _parser(xmlfile)
