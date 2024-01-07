from datetime import datetime
from pathlib import Path
from urllib import parse as parse

import requests

import src.helpers.write as write


def fetch_rss(
    url: str,
    path: Path = Path.cwd(),
    period: datetime = datetime.now(),
    head: bool = False,
    overwrite: bool = False,
) -> int:
    # create the file name and add it to the path
    if path.exists():
        fn = write.write_fn(period=period)
        path = path.joinpath(fn)
    else:
        msg = "The directory des not exist.\n{path}"
        raise FileNotFoundError(msg)

    # don't process a file that already exists unless required
    if not head and path.exists() and not overwrite:
        msg = "File already exists and will not be overwritten.\n"
        msg += 'This can be changed with the argument "overwrite".\n'
        msg += f"{fn}"
        raise FileExistsError(msg)

    # add filename to the url
    url_fn = parse.urljoin(url, fn)

    # make the request
    if not head:
        with requests.get(url_fn) as r:
            with path.open(mode="w") as f:
                if r.status_code == 200:
                    f.write(r.text)
    else:
        with requests.head(url_fn) as r:
            pass

    return r.status_code
