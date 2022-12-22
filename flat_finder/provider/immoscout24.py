from flat_finder.models import ProviderConfig, Downloader, CrawlFields, ParsedFlat


def process_flat(flat: ParsedFlat) -> ParsedFlat:
    return ParsedFlat(
        id=flat.id,
        price=flat.price,
        size=flat.size,
        title=flat.title.replace("NEU", "").strip(),
        link=f'https://www.immobilienscout24.de{flat.link}',
        address=flat.address,
        image=flat.image
    )


IMMOSCOUT_24_CONFIG = ProviderConfig(
    name="IMMOSCOUT_24",
    base_url="https://www.immobilienscout24.de/",
    downloader=Downloader.SCRAPING_BEE,
    paginate_next_button_selector="""
        var element = document.querySelector("ul.reactPagination li[class='p-items p-next vertical-center-container'] a");
        
        if (!element) {
            return false;
        }
        
        element.click();
        
        return true;
        """,
    cookie_banner_button_selector="""return document.querySelector('#usercentrics-root')?.shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""",
    headless=False,
    crawl_container="#resultListItems > li[class='result-list__listing'] article",
    crawl_fields=CrawlFields(
        id='@data-obid',
        price='.result-list-entry__criteria .grid-item:first-child dd',
        size='.result-list-entry__criteria .grid-item:nth-child(2) dd',
        title='.result-list-entry__brand-title-container h5',
        link='.result-list-entry__brand-title-container@href',
        address='.result-list-entry__map-link',
        image=""
    ),
    process_flat=process_flat,
    retries=3
)
