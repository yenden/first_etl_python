import logging
import sqlite3
from typing import Dict, Any

from common.loader import Loader
import pandas as pd


class Sqlite3Loader(Loader):

    def __init__(self, destination_config: Dict[str, Any]) -> None:
        super().__init__(destination_config)
        try:
            self.connection = sqlite3.connect(self.config["host"])
        except sqlite3.Error as e:
            print(e)
            logging.getLogger(__name__).error(e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def __del__(self):
        if self.connection:
            self.connection.close()
    def load(self, data: pd.DataFrame, table: str):
        data.to_sql(table, self.connection, if_exists="replace")
