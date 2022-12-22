from flat_finder.models import ProviderConfig, Downloader, CrawlFields

IMMOWELT_CONFIG = ProviderConfig(
    name="IMMOWELT",
    base_url="https://www.immowelt.de/",
    downloader=Downloader.SIMPLE,
    crawl_container="div[class^='EstateItem-']",
    crawl_fields=CrawlFields(
        id='a@id',
        price="div[class^='KeyFacts-'] [data-test='price']",
        size="div[class^='KeyFacts-'] [data-test='area']",
        title="div[class^='FactsMain-'] h2",
        link='a@href',
        address="div[class^='estateFacts-'] span",
        image=""
    )
)
