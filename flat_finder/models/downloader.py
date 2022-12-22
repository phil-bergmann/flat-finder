from abc import ABC, abstractmethod

from . import ParsedFlat


class AbstractDownloader(ABC):

    @abstractmethod
    def get_html(self) -> [str]:
        raise NotImplementedError("Implement this!")