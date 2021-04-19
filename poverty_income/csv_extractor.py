""" """
from typing import Any
import pandas as pd
from common.extractor import Extractor


class CSVExtractor(Extractor):

    def extract(self) -> Any:
        return pd.read_csv(self.config["poverty"], skiprows=2)



