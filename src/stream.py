from justwatch import JustWatch

from models import Query
from values import PLATFORMS, REGIONS


class SteamerFinder:
    def __init__(self, country: str, query: Query):
        if country not in REGIONS:
            raise ValueError(f"Region {country} not supported")
        self.region = country
        self.query = query.value
        self.results = self.search()
        self.title = self.results["title"]
        self.offers = self.results["offers"]
        
    def search(self):
        jw_api = JustWatch(country=self.region).search_for_item(query=self.query)
        if not jw_api["items"]:
            raise ValueError(f"No results found for {self.query}")
        return jw_api["items"][0]

    def get_streamer_offers(self):
        return [
            {
                "platform": PLATFORMS[i["package_short_name"]],
                "url": i["urls"]["standard_web"],
            }
            for i in self.results["offers"]
            if i["monetization_type"] == "flatrate"
        ]

    def get_platforms(self):
        return {p["platform"]: p["url"] for p in self.get_streamer_offers()}
