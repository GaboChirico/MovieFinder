from typing import Dict, List

from justwatch import JustWatch

from models import Result
from serialize import serialize
from values import PLATFORMS


def find(query: str, region: str) -> Result:
    return serialize(SteamerFinder(query=query, region=region)())


class SteamerFinder:
    def __init__(self, query: str, region: str):
        self.query = query
        self.region = region
        self.results = Result()

    def __call__(self):
        payload = self.search()
        self.results.title = self.get_title(payload)
        self.results.platforms = self.get_platforms(payload)
        return self.results

    def search(self) -> Dict[str, str]:
        jw_api = JustWatch(country=self.region).search_for_item(query=self.query)
        return jw_api["items"][0]

    @staticmethod
    def get_title(payload: Dict[str, str]) -> str:
        return payload["title"]

    @staticmethod
    def get_platforms(payload: Dict[str, str]) -> List[Dict[str, str]]:
        platforms = [
            {
                "platform": PLATFORMS[i["package_short_name"]],
                "url": i["urls"]["standard_web"],
            }
            for i in payload["offers"]
            if i["monetization_type"] == "flatrate"
            and i["package_short_name"] in PLATFORMS
        ]
        return [dict(t) for t in {tuple(d.items()) for d in platforms}]
