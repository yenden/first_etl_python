""" """
from typing import Any

import requests
import pandas as pd
from common.extractor import Extractor


class APIExtractor(Extractor):

    def extract(self) -> Any:
        return pd.DataFrame(requests.get(self.config["income"]).json()['BEAAPI']['Results']['Data'])



