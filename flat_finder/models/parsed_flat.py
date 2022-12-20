from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ParsedFlat:
    id: str
    price: str
    size: str
    title: str
    link: str
    address: str
    image: Optional[str]
