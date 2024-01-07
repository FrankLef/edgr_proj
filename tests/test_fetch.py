from datetime import datetime
from pathlib import Path
from urllib import parse as parse

import pytest

from config import settings

# from src.edgaretl import registry
# from src.edgaretl.xbrlrss import write
# from src.edgaretl.xbrlrss import fetch
from src.helpers import fetch, write


@pytest.fixture
def dir_2020():
    project_path = Path(__file__).parent.parent
    data_path = Path.joinpath(project_path, "data", "test")
    return data_path


@pytest.fixture
def test_url():
    return settings.url.example


@pytest.fixture
def edgar_url():
    return settings.url.edgar


@pytest.fixture
def month_url():
    return settings.url.edgar_month


@pytest.fixture
def oldmonth_url():
    return settings.url.edgar_month_old


@pytest.fixture
def specs(dir_2020, month_url):
    per = datetime(2020, 1, 1)
    a_dir = Path(dir_2020)
    fn = write.write_fn(period=per)
    path = a_dir.joinpath(fn)
    # url = month_url
    # url_fn = url + r"/" + fn
    url_fn = parse.joinurl(month_url, fn)
    specs = {
        "period": per,
        "dir": a_dir,
        "file": fn,
        "path": path,
        "url": month_url,
        "url_fn": url_fn,
    }
    return specs


def test_fetch_rss_err_dir(test_url):
    with pytest.raises(FileNotFoundError):
        assert fetch.fetch_rss(url=test_url, path=Path.cwd().joinpath("WRONG"))


def test_fetch_rss_head_oldmonth(oldmonth_url, specs):
    assert fetch.fetch_rss(
        url=oldmonth_url, path=specs["dir"], period=specs["period"], head=True
    ) in {301, 403}


def test_fetch_rss_head_month(specs):
    assert fetch.fetch_rss(
        url=specs["url"], path=specs["dir"], period=specs["period"], head=True
    ) in {200, 403}


# only done from time to time as it takes resources
@pytest.mark.skip(reason="too slow, do it only if necessary")
def test_fetch_rss(specs):
    assert fetch.fetch_rss(
        url=specs["url"],
        path=specs["dir"],
        period=specs["period"],
        overwrite=True,
    ) in {200, 403}


def test_fetch_rss_err_exists(specs):
    with pytest.raises(FileExistsError):
        assert fetch.fetch_rss(
            url=specs["url"],
            path=specs["dir"],
            period=specs["period"],
            overwrite=False,
        )
