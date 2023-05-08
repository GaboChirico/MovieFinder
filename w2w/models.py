from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Query:
    value: str
    region: str


@dataclass
class Result:
    title: str = field(default_factory=str)
    platforms: Dict[str, str] = field(default_factory=dict)

    def __str__(self):
        return str(self.__dict__)
