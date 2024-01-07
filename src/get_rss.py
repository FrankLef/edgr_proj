import logging
import sys
from datetime import datetime
from pathlib import Path

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)
log = logging.getLogger("rich")

src_path = Path(__file__).parent
if src_path not in sys.path:
    sys.path.insert(1, str(src_path))

project_path = src_path.parent
if src_path not in sys.path:
    sys.path.insert(1, str(project_path))

from config import settings  # noqa
from src.helpers import fetch  # noqa

the_url = settings.url.edgar_month
the_period = datetime(2023, 12, 1)
the_data_path = project_path.joinpath("data", "raw")


def get_rss(
    url: str, path: Path, period: datetime, head: bool, overwrite: bool
) -> int:
    log.debug(
        "url = %s\npath = %s\nperiod = %s",
        url,
        path,
        datetime.strftime(period, "%Y-%m"),
    )
    status_code = fetch.fetch_rss(
        url, path, period, head=head, overwrite=overwrite
    )
    # status_code = 0
    return status_code


out = get_rss(
    url=the_url,
    path=the_data_path,
    period=the_period,
    head=False,
    overwrite=True,
)

log.debug("status code = %d", out)
