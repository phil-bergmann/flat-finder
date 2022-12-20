from flat_finder.models import ProviderConfig, Downloader, CrawlFields, ParsedFlat


def process_flat(flat: ParsedFlat) -> ParsedFlat:
    return ParsedFlat(
        id=flat.id.replace("selObject_", ""),
        price=flat.price,
        size=flat.size,
        title=flat.title.replace("NEU", "").strip(),
        link=f'https://www.immonet.de/angebot/{flat.id.replace("selObject_", "")}',
        address=flat.address.split(' • ')[len(flat.address.split(' • ')) - 1]
    )


IMMONET_CONFIG = ProviderConfig(
    name="IMMONET",
    base_url="https://www.immonet.de/",
    downloader=Downloader.SELENIUM,
    paginate_next_button_selector="""return document.getElementsByClassName("col-sm-3 col-xs-1 pull-right text-right")""",
    cookie_banner_button_selector="""return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""",
    headless=False,
    crawl_container='#result-list-stage .item',
    crawl_fields=CrawlFields(
        id='@id',
        price='div[id*="selPrice_"]',
        size='div[id*="selArea_"]',
        title='.item a.block.ellipsis.text-225.text-default',
        address='.item .box-25 .ellipsis .text-100',
        link=None,
        image=""
    ),
    process_flat=process_flat
)
