""" """
from abc import ABC, abstractmethod
from typing import Any


class Transformer(ABC):

    @abstractmethod
    def transform(self, data) -> Any:
        pass
