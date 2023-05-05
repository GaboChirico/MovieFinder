from dataclasses import dataclass
from typing import Dict


@dataclass
class Query:
    value: str


@dataclass
class Result:
    title: str
    platforms: Dict[str, str]
