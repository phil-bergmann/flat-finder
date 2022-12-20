from bs4 import BeautifulSoup

from flat_finder.models import ParsedFlat, ProviderConfig, ParseException


def parse_html(config: ProviderConfig, html: str) -> [ParsedFlat]:
    soup = BeautifulSoup(html, 'html.parser')
    containers = soup.select(config.crawl_container)

    if len(containers) == 0:
        return []

    fields = config.crawl_fields
    flats = []

    for c in containers:
        try:
            flat = ParsedFlat(
                id=_parse_element(c, fields.id),
                price=_parse_element(c, fields.price),
                size=_parse_element(c, fields.size),
                title=_parse_element(c, fields.title),
                link=_parse_element(c, fields.link) if fields.link else "ADDED LATER",
                address=_parse_element(c, fields.address),
                image=_parse_element(c, fields.image, require_non_null=False)
            )
            flats.append(config.process_flat(flat))
        except ParseException as e:
            print(e)

    return flats

def _parse_element(container, selector: str, require_non_null=True):
    path = selector.split("@")[0]

    element = container

    if len(path.strip()) > 0:
        elements = element.select(path)

        if len(elements) == 0:
            if require_non_null:
                raise ParseException(f"Element {selector} not found:\n{container}")
            else:
                return None
        element = elements[0]

    if len(selector.split("@")) > 1:
        tag = selector.split("@")[1]
        element = element.get(tag)
    else:
        element = element.text

    element = element.replace("\n", " ").replace("\t", " ")

    while True:
        element_repl = element.replace("  ", " ")
        if element_repl == element:
            break
        element = element_repl

    return element.strip()
