# Feedler

A dead simple parser.

This package is intended to be used as a global parser mainly for rss feeds.

## Setup

```
pip install feedler
```

## Usage

```python
from feedler.parsers import rss_parser

# parse from a url
rss_dict = rss_parser("https://sample.url")

# parse from a file
rss_dict = rss_parser("/path/to/file")

# get the rss as json
rss_json = rss_parser("url or file_path", format="json")
```

## Test

First you need to clone this repo

```
git clone git@github.com:xheuz/feedler.git
```

Then you need to add a virtualenv

```bash
python3 -m virtualenv ./.venv

# activate your venv
source .venv/bin/activate

# install all requirements.txt
pip install -r requirements.txt
```

And last run the tests

```
export PYTHONPATH=${PWD}; pytest -v .
```
