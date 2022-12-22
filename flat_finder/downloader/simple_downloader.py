import requests

from flat_finder.models import AbstractDownloader, ProviderConfig


class SimpleDownloader(AbstractDownloader):

    def __init__(self, config: ProviderConfig, url: str):
        self.url = url
        self.paginate_next_button_selector = config.paginate_next_button_selector
        self.cookie_banner_button_selector = config.cookie_banner_button_selector

    def get_html(self) -> [str]:
        response = requests.get(self.url)
        return [response.text]