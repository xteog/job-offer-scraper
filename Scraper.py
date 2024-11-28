import json
import logging
from urllib.parse import urljoin
import requests
from lxml import html
from utils import Offer, Site



class Scraper:
    def __init__(self, site: Site) -> None:
        self.site = site

    def getOffers(self) -> list[Offer]:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "content-type":"text/plain"
        }

        if self.site.body == "":
            response = requests.get(self.site.url, headers=headers)
        else:
            response = requests.post(self.site.url, headers=headers, data=self.site.body)

        if response.status_code == 200:
            content = response.content
        else:
            content = ""
            logging.error(f"Failed to retrieve page. Status code: {response.status_code}")

        return self.scrapContent(content=content)
    
    def scrapContent(self, content: str) -> list[Offer]:
        pass

class ScraperReq(Scraper):
    def __init__(self, site: Site) -> None:
        super().__init__(site)

    def scrapContent(self, content: str) -> list[Offer]:
        offers = []

        content = json.loads(content)

        for offer in content["results"][0]["hits"]:
            name = offer["name"]
            link = "https://www.lvmh.com/join-us/our-job-offers/" + offer["objectID"]
            offers.append(Offer(name=name, link=link))

        return offers
    


class ScraperWeb(Scraper):
    def __init__(self, site: Site) -> None:
        super().__init__(site)

    def scrapContent(self, content: str) -> list[Offer]:
        xpath_list = self.site.paths["xpath_list"]
        xpath_offer_name = self.site.paths["xpath_offer_name"]
        xpath_offer_link = self.site.paths["xpath_offer_link"]

        tree = html.fromstring(content)

        results = tree.xpath(xpath_list)

        n = len(results)


        results = []
        for i in range(n):
            name = tree.xpath(xpath_offer_name.format(index=i))

            if len(name) == 0:
                continue

            name = name[0].replace("\n", "")

            link = tree.xpath(xpath_offer_link.format(index=i))
            link = link[0]

            if link.find("https") == -1:
                link = urljoin(self.site.url, link)

            results.append(Offer(name=name, link=link))

        return results