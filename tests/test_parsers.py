import pytest
from feedler.parsers import rss_parser


def test_rss_file_can_be_converted_to_dict():
    rss = rss_parser("/Users/victornatschke/Downloads/feedburner.xml")

    assert isinstance(rss, dict)


def test_rss_feed_url_can_be_converted_to_dict():
    rss = rss_parser("https://nyaa.net/feed?c=3_5&q=720")

    assert isinstance(rss, dict)


def test_bad_url_raise_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        rss_parser("https://invalid/url")


def test_bad_file_path_raise_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        rss_parser("/bad/path/to/file")
