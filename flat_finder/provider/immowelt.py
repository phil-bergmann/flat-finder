from flat_finder.models import ProviderConfig, Downloader, CrawlFields

IMMOWELT_CONFIG = ProviderConfig(
    name="IMMOWELT",
    base_url="https://www.immowelt.de/",
    downloader=Downloader.SELENIUM,
    paginate_next_button_selector="""
        var aTags = document.getElementsByClassName("navNumberButton-d264f");
        var searchText = "{i}";
        var found;

        for (var i = 0; i < aTags.length; i++) {
            if (aTags[i].textContent == searchText) {
                return aTags[i];
            }
        }""",
    cookie_banner_button_selector="""return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""",
    headless=False,
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
