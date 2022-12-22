from abc import ABC, abstractmethod

from . import ParsedFlat


class AbstractDownloader(ABC):

    @abstractmethod
    def get_html(self, url: str) -> [str]:
        raise NotImplementedError("Implement this!")