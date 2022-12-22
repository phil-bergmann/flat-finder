import os

import requests
from urllib.parse import quote

from flat_finder.models import AbstractDownloader


class ScrapingbeeDownloader(AbstractDownloader):

    def __init__(self):
        self.token = os.environ['SCRAPING_BEE_TOKEN']

    def get_html(self, url: str) -> [str]:
        encoded = quote(url, safe='')
        try:
            response = requests.get(f"https://app.scrapingbee.com/api/v1/?api_key={self.token}&stealth_proxy=True&render_js=True&url={encoded}", timeout=120)
        except Exception as e:
            print(f"Error connecting to scrapingbee:\n{e}")
            return []

        if response.status_code // 100 != 2:
            print(f"Error in scrapingbee downloader: {response.status_code}")
            return []

        return [response.text]