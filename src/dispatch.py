import logging
import sys
from pathlib import Path

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)
log = logging.getLogger("rich")

# src path
src_path = Path(__file__).parent
# add the project path to be able to access the settings
a_path = src_path.parent
if a_path not in sys.path:
    sys.path.insert(1, str(a_path))

from config import settings  # noqa

a_url = settings.url.simple


def main(text: str, n: int) -> bool:
    log.info("Dispatching '%s' with n = %d.", text, n)
    log.debug(a_url)
    return True
