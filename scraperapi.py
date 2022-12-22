from flat_finder import Processor
from dotenv import load_dotenv
import os

from flat_finder.adapters import SlackAdapter


URL = "https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?numberofrooms=2.0-&price=-1800.0&livingspace=60.0-&exclusioncriteria=swapflat&pricetype=rentpermonth&geocodes=0916200017,0916200016,0916200013051,0916200013050,0916200014060,0916200025008,0916200014070,0916200010033,0916200014048,0916200010,0916200013,0916200015,0916200010032,0916200014,0916200025,0916200025075&sorting=2&enteredFrom=result_list"
def soup():
    from scraper_api import ScraperAPIClient
    client = ScraperAPIClient('a957d7bd6a89f57fda96640fca7f1156')
    result = client.get(url=URL, country_code="DE", premium=True, render=True).text

    print(result)

if __name__ == "__main__":
    soup()