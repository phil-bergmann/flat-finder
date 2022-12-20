import json
import os
from datetime import timedelta, datetime
import time
from typing import Optional
from os import path

from flat_finder.adapters import SlackAdapter
from flat_finder.downloader import SeleniumDownloader
from flat_finder.parser import parse_html
from flat_finder.provider import ALL_CONFIGS
from flat_finder.models import ProviderConfig, Downloader, ParsedFlat, AbstractAdapter


class Processor:

    def __init__(self):
        self.urls = json.loads(os.environ['URLS'])
        self.adapter: AbstractAdapter = SlackAdapter()

        self.refresh_every_minutes = int(os.environ['REFRESH_EVERY_MINUTES'])

        self.sent_flats = set()

        if path.exists("sent_flats.txt"):
            with open("sent_flats.txt", "r") as in_file:
                for l in in_file.readlines():
                    self.sent_flats.add(l.strip())

    def run(self,):
        last_run: Optional[datetime] = None

        while True:
            if last_run is not None and last_run + timedelta(minutes=self.refresh_every_minutes) > datetime.now():
                time.sleep(10)
                continue

            last_run = datetime.now()

            self._process_urls()

    def _process_urls(self):
        for u in self.urls:
            config = Processor._find_config_for_url(u)

            if config is None:
                print(f"[!] Skipping as no config was found: {u}")
                continue

            htmls = Processor._download(config, u)

            flats = [f for h in htmls for f in parse_html(config, h)]

            print(f"{config.name}: {len(flats)} flats")

            for f in flats:
                self._send_to_adapter_if_missing(config, f)

    @staticmethod
    def _find_config_for_url(url: str) -> Optional[ProviderConfig]:
        for c in ALL_CONFIGS:
            if c.base_url in url:
                return c

        return None

    @staticmethod
    def _download(config: ProviderConfig, url: str) -> [str]:
        if config.downloader == Downloader.SELENIUM:
            return SeleniumDownloader(config, url).get_html()
        else:
            print(f"[!] Downloader not supported: {config.downloader}")
            return []

    def _send_to_adapter_if_missing(self, config: ProviderConfig, flat: ParsedFlat):
        flat_id = f"{config.name}-{flat.id}"

        if flat_id in self.sent_flats:
            return

        sent = self.adapter.send_flat(flat)

        if sent:
            self.sent_flats.add(flat_id)

            with open("sent_flats.txt", "a") as out_file:
                out_file.write(flat_id)
                out_file.write("\n")







