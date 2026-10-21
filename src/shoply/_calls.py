"""What a call of a route is made of: its address, and where its fields go."""

import urllib.parse
from typing import Any, Dict, List, Optional, Tuple

from ._generated.routes import ROUTES


def prepare(id: str, path: List[str], fields: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, str], Optional[Dict[str, Any]], Any, Optional[Tuple[str, Any, Optional[str], Optional[str]]]]:
    """The route, the address's IDs by name, and the fields: as the query, the JSON body, or a file."""
    route = ROUTES[id]
    values: Dict[str, str] = {}

    for index, name in enumerate(route["params"]):
        value = path[index] if index < len(path) else ""
        if not isinstance(value, str) or value == "":
            raise ValueError(f"{id} needs {name}.")
        values[name] = value

    given = {name: value for name, value in fields.items() if value is not None}
    query: Optional[Dict[str, Any]] = None
    body: Any = None
    form = None

    if route["upload"]:
        form = (route["upload"], given.get("file"), given.get("filename"), given.get("content_type"))
        # What the route takes beside the file (a dispute's file says its `kind`) is in the address.
        query = {name: value for name, value in given.items() if name in route["query"]}
    elif route["body"]:
        query = {name: value for name, value in given.items() if name in route["query"]}
        body = {name: value for name, value in given.items() if name not in route["query"]}
    else:
        query = given

    return route, values, query, body, form


def fill(template: str, values: Dict[str, str]) -> str:
    """The route's address with its IDs in it, each escaped."""
    for name, value in values.items():
        template = template.replace("{" + name + "}", urllib.parse.quote(value, safe=""))
    return template
