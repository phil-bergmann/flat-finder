from typing import Optional

import undetected_chromedriver as uc
import time

from bs4 import BeautifulSoup

from flat_finder.models import ProviderConfig


class SeleniumDownloader:

    def __init__(self, config: ProviderConfig, url: str):
        self.url = url
        self.paginate_next_button_selector = config.paginate_next_button_selector
        self.cookie_banner_button_selector = config.cookie_banner_button_selector
        self.headless = config.headless

    def get_html(self) -> [str]:
        options = uc.ChromeOptions()

        if self.headless:
            options.headless = True
        # options.add_argument('--headless')
        chrome = uc.Chrome(options=options)
        chrome.get(self.url)
        time.sleep(5)

        if self.cookie_banner_button_selector:
            element = chrome.execute_script(self.cookie_banner_button_selector)
            if element:
                element.click()
        time.sleep(5)

        htmls = [chrome.page_source]

        page = 1
        while True:
            page += 1
            element = chrome.execute_script(self.paginate_next_button_selector.replace("{i}", str(page)))

            if not element:
                break

            element.click()
            time.sleep(5)
            htmls.append(chrome.page_source)


        chrome.close()

        return htmls
