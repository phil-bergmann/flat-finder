import json
import os
from datetime import timedelta, datetime
import time
from typing import Optional
from os import path

from flat_finder.adapters import SlackAdapter, TelegramAdapter
from flat_finder.downloader import ScrapingbeeDownloader, SimpleDownloader
from flat_finder.parser import parse_html
from flat_finder.provider import ALL_CONFIGS
from flat_finder.models import ProviderConfig, Downloader, ParsedFlat, AbstractAdapter


class Processor:

    def __init__(self, config_path: str):
        self.urls = json.loads(os.environ['URLS'])
        self.adapters: [AbstractAdapter] = []

        if os.environ['TELEGRAM_BOT_ACTIVE']:
            self.adapters.append(TelegramAdapter())

        if os.environ['SLACK_BOT_ACTIVE']:
            self.adapters.append(SlackAdapter())

        self.refresh_every_minutes = int(os.environ['REFRESH_EVERY_MINUTES'])
        self.retries = int(os.environ['RETRIES'])

        self.sent_flats_path = f"{config_path}/sent_flats.txt"

        self.sent_flats = set()

        if path.exists(self.sent_flats_path):
            with open(self.sent_flats_path, "r") as in_file:
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

            flats = []
            calls = 0

            while calls <= self.retries and len(flats) == 0:
                htmls = Processor._download(config, u)
                flats = [f for h in htmls for f in parse_html(config, h)]
                calls += 1

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
        if config.downloader == Downloader.SCRAPING_BEE:
            return ScrapingbeeDownloader().get_html(url)
        elif config.downloader == Downloader.SIMPLE:
            return SimpleDownloader().get_html(url)
        else:
            print(f"[!] Downloader not supported: {config.downloader}")
            return []

    def _send_to_adapter_if_missing(self, config: ProviderConfig, flat: ParsedFlat):
        flat_id = f"{config.name}-{flat.id}"

        if flat_id in self.sent_flats:
            return

        sent = False
        for a in self.adapters:
            sent |= a.send_flat(flat)

        if sent:
            self.sent_flats.add(flat_id)

            with open(self.sent_flats_path, "a") as out_file:
                out_file.write(flat_id)
                out_file.write("\n")
