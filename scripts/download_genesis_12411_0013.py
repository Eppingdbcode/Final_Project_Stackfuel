"""Download the approved GENESIS hero export using an API token.

The token is read only from GENESIS_API_TOKEN and is never persisted. The
script refuses to overwrite an existing RAW file.
"""

from __future__ import annotations

import argparse
import os
import urllib.parse
import urllib.request
from pathlib import Path

URL = "https://genesis.destatis.de/genesisWS/rest/2020/data/tablefile"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f"Refusing to overwrite RAW: {args.output}")
    token = os.environ.get("GENESIS_API_TOKEN")
    if not token:
        raise RuntimeError("GENESIS_API_TOKEN is required")
    body = urllib.parse.urlencode({
        "name": "12411-0013", "startyear": "2021", "endyear": "2025",
        "compress": "true", "transpose": "false", "format": "ffcsv", "language": "de",
    }).encode()
    request = urllib.request.Request(URL, data=body, method="POST", headers={
        "Content-Type": "application/x-www-form-urlencoded", "username": token, "password": "",
    })
    with urllib.request.urlopen(request, timeout=120) as response:
        content = response.read()
    if not content.startswith(b"PK"):
        raise ValueError("GENESIS response is not a ZIP; refusing to persist it")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(content)


if __name__ == "__main__":
    main()
