from datetime import datetime
from pathlib import Path

import feedparser
import pytest

from config import settings


@pytest.fixture
def dir_2020():
    return settings.path.rss2020


@pytest.fixture
def file_2020():
    project_path = Path(__file__).parent.parent
    data_path = Path.joinpath(project_path, "data", "test")
    fn = data_path.joinpath(settings.file.rss202001)
    return fn


@pytest.fixture
def data2020():
    """Dictionary of target data from xbrlrss-2020-01.xml."""
    data = {
        "channel": {
            "items_nb": 2859,
            "language": "en-us",
            "pubDate": datetime(2020, 1, 31, 5, 0),
            "title": "All XBRL Data Submitted to the SEC for 2020-01",
        },
        "item0": {
            "edgar:accessionNumber": "0001193125-20-021708",
            "edgar:cikNumber": "0001631650",
            "edgar:companyName": "Aimmune Therapeutics, Inc.",
            "edgar:fiscalyearend": "1231",
            "edgar:formType": "8-K",
            "edgar:period": "20200131",
            "enclosure_len": "18012",
            "enclosure_url": "https://www.sec.gov/Archives/edgar/data/1631650/000119312520021708/0001193125-20-021708-xbrl.zip",
            "pubDate": datetime(2020, 1, 31, 22, 29, 40),
            "title": "Aimmune Therapeutics, Inc. (0001631650) (Filer)",
        },
    }
    return data


@pytest.fixture
def fpd2020(file_2020):
    """Create a feed parser dictionary from xbrlrss-2020-01.xml."""
    return feedparser.parse(file_2020)


def test_feed(fpd2020, data2020):
    assert isinstance(fpd2020, feedparser.util.FeedParserDict)
    assert len(fpd2020.entries) == data2020["channel"]["items_nb"]
