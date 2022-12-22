from typing import Optional

import undetected_chromedriver as uc
import time
import random

from bs4 import BeautifulSoup

from flat_finder.utils import sample
from flat_finder.models import ProviderConfig, AbstractDownloader


class SeleniumDownloader(AbstractDownloader):

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
        # options.add_argument('--proxy-server=%s' % PROXY)
        chrome = uc.Chrome(options=options)
        chrome.get(self.url)
        time.sleep(sample(5, 3))

        if self.cookie_banner_button_selector:
            element = chrome.execute_script(self.cookie_banner_button_selector)
            if element:
                element.click()
        time.sleep(sample(5, 3))

        htmls = [chrome.page_source]

        page = 1
        while True:
            #SeleniumDownloader.scroll_down(chrome)

            page += 1
            element = chrome.execute_script(self.paginate_next_button_selector.replace("{i}", str(page)))

            if not element:
                break

            time.sleep(sample(6, 3))
            htmls.append(chrome.page_source)


        chrome.close()

        return htmls

    @staticmethod
    def scroll_down(chrome):

        # Get scroll height
        last_height = 0

        while True:
            # Scroll down to bottom
            chrome.execute_script(f"window.scrollTo(0, {last_height + sample(150, 50)});")

            # Wait to load page
            time.sleep(sample(0.5, 0.5))

            # Calculate new scroll height and compare with last scroll height
            new_height = chrome.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
