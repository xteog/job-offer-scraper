import json


def read(path: str) -> dict:
    with open(path, "r") as f:
        file = f.read()
    return json.loads(file)


def write(path: str, data: list) -> None:
    data = json.dumps(data, indent=2)
    with open(path, "w+") as f:
        f.write(data)


class Site:
    def __init__(self) -> None:
        self.url = ""
        self.paths = {
            "xpath_list": "",
            "xpath_offer_name": "",
            "xpath_offer_link": "",
        }
        self.body = ""


class Offer:
    def __init__(self, name: str, link: str) -> None:
        self.name = name
        self.link = link
