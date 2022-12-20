from flat_finder import Processor
from dotenv import load_dotenv
import os

from flat_finder.adapters import SlackAdapter

URLS = ["https://www.immowelt.de/liste/muenchen-altstadt-lehel/wohnungen/mieten?d=true&pma=2000&r=3&rmi=2&sd=DESC&sf=RELEVANCE&sp=1"]

def soup():
    load_dotenv()
    p = Processor(URLS, SlackAdapter(channel="#flat-finder"))
    p.run(5)

if __name__ == "__main__":
    soup()