from dataclasses import dataclass
from enum import Enum
from typing import Optional, Callable

from flat_finder.models import ParsedFlat


class Downloader(Enum):
    SELENIUM = 1
    SCRAPING_BEE = 2


@dataclass(frozen=True)
class CrawlFields:
    id: str
    price: str
    size: str
    title: str
    link: Optional[str]
    address: str
    image: str

@dataclass(frozen=True)
class ProviderConfig:
    name: str
    base_url: str
    downloader: Downloader
    headless: bool
    paginate_next_button_selector: str
    crawl_container: str
    crawl_fields: CrawlFields
    cookie_banner_button_selector: Optional[str] = None
    process_flat: Callable[[ParsedFlat], ParsedFlat] = lambda x: x



    