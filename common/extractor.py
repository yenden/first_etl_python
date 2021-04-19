""" """
from abc import ABC, abstractmethod
from typing import Any, Dict


class Extractor(ABC):

    def __init__(self, source_config: Dict[str, Any]) -> None:
        self.config = source_config

    @abstractmethod
    def extract(self) -> Any:
        pass
