from typing import Optional


class SimpleDownloader:

    def __int__(self, url: str, paginate_next_button_selector: str, cookie_banner_button_selector: Optional[str]):
        self.url = url
        self.paginate_next_button_selector = paginate_next_button_selector
        self.cookie_banner_button_selector = cookie_banner_button_selector