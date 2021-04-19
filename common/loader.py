from abc import ABC, abstractmethod
from typing import Dict, Any


class Loader(ABC):
    def __init__(self, destination_config: Dict[str, Any]) -> None:
        self.config = destination_config

    @abstractmethod
    def load(self, data, table):
        pass
