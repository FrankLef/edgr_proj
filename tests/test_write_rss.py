from datetime import datetime as dt

import pytest

from config import settings
from src.helpers.write import write_fn


@pytest.fixture
def prefix():
    return settings.file_prefix


@pytest.fixture
def get_url():
    return settings.url.example


def test_write_fn(prefix):
    """write_fn()"""
    period = dt.now()
    target = "-".join((prefix, dt.strftime(period, "%Y-%m"))) + ".xml"
    out = write_fn(period=period)
    assert out == target


@pytest.mark.parametrize("per", [dt(2005, 3, 31), dt(2100, 1, 1)])
def test_write_fn_err_period(per):
    """write_fn() with invalid periods"""
    with pytest.raises(ValueError):
        write_fn(period=per)
