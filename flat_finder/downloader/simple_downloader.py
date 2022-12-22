import requests

from flat_finder.models import AbstractDownloader


class SimpleDownloader(AbstractDownloader):

    def get_html(self, url: str) -> [str]:
        try:
            response = requests.get(url)
        except Exception as e:
            print(f"Error in simple downloader:\n{e}")
            return []

        if response.status_code // 100 != 2:
            print(f"Error in simple downloader: {response.status_code}")
            return []

        return [response.text]