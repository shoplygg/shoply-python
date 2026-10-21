import os
from typing import Dict, Optional, Union


class File:
    """A route's answer that is a file, a CSV or a PDF, as it came: `body` its bytes, `headers` by
    lowercase name."""

    def __init__(self, body: bytes, headers: Dict[str, str]) -> None:
        self.body = body
        self.headers = headers

    @property
    def content_type(self) -> Optional[str]:
        """Its type, "text/csv"."""
        return self.headers.get("content-type")

    def text(self, encoding: str = "utf-8-sig") -> str:
        """Its body as text. A CSV from Shoply starts with a byte order mark, for spreadsheets,
        which this leaves out."""
        return self.body.decode(encoding)

    def save(self, path: Union[str, "os.PathLike[str]"]) -> None:
        """Written to a file."""
        with open(path, "wb") as handle:
            handle.write(self.body)
