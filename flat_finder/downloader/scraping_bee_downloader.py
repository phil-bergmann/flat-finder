import os
from typing import Optional

import requests
from scrapingbee import ScrapingBeeClient
from urllib.parse import quote

from flat_finder.models import AbstractDownloader, ProviderConfig


class ScrapingbeeDownloader(AbstractDownloader):

    def __init__(self, config: ProviderConfig, url: str):
        self.url = url
        self.paginate_next_button_selector = config.paginate_next_button_selector
        self.cookie_banner_button_selector = config.cookie_banner_button_selector
        self.token = os.environ['SCRAPING_BEE_TOKEN']

        #self.client = ScrapingBeeClient(api_key=os.environ['SCRAPING_BEE_TOKEN'])

    def get_html(self) -> [str]:
        encoded = quote(self.url, safe='')
        try:
            response = requests.get(f"https://app.scrapingbee.com/api/v1/?api_key={self.token}&stealth_proxy=True&render_js=True&url={encoded}", timeout=60)
        except Exception as e:
            print(f"Error connecting to scrapingbee:\n{e}")
            return []

        #response = self.client.get(self.url, params={
        #    'render_js': 'True',
        #    'stealth_proxy': 'True'
        #})

        return [response.text]