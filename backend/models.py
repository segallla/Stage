from dataclasses import dataclass
from typing import List


@dataclass
class Datasource:
    """Metadata for a datasource."""

    name: str
    fields: List[str]
    tags: List[str]
    geom_type: str


datasources = [
    Datasource(name="roads", fields=["id", "name"], tags=["osm"], geom_type="LINESTRING"),
]
