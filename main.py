import config
from emails import sendEmail
import logging
import utils


logging.basicConfig(
    filename="log.log",
    format="%(asctime)s [%(levelname)s]:%(name)s:%(message)s",
    level=logging.INFO,
)

offers = []
for scraper in config.scrapers:
    offers += scraper.getOffers()

offers_sent = utils.read(path="offers_sent.json")

for offer in offers:
    if offer.link in offers_sent:
        continue

    sendEmail(subject=f"[Job Offer] {offer.name}", body=offer.link)

    offers_sent.append(offer.link)

    utils.write(path="offers_sent.json", data=offers_sent)
