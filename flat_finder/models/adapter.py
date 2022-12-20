from abc import ABC, abstractmethod

from . import ParsedFlat


class AbstractAdapter(ABC):

    @abstractmethod
    def send_flat(self, flat: ParsedFlat) -> bool:
        raise NotImplementedError("Implement this!")