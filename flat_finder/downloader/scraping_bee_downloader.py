import os
from typing import Optional
from scrapingbee import ScrapingBeeClient
from urllib.parse import quote

from flat_finder.models import AbstractDownloader, ProviderConfig


class ScrapingbeeDownloader(AbstractDownloader):

    def __init__(self, config: ProviderConfig, url: str):
        self.url = url
        self.paginate_next_button_selector = config.paginate_next_button_selector
        self.cookie_banner_button_selector = config.cookie_banner_button_selector

        self.client = ScrapingBeeClient(api_key=os.environ['SCRAPING_BEE_TOKEN'])

    def get_html(self) -> [str]:
        response = self.client.get(self.url, params={
            'render_js': 'True',
            'stealth_proxy': 'True'
        })
        return [response.text]