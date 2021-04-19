from typing import Any

from common.transformer import Transformer
import pandas as pd
import copy


class APITransformer(Transformer):
    def transform(self, data) -> Any:
        # keep only interesting columns
        income_df_clean = copy.deepcopy(data[["GeoFips", "DataValue"]])
        # transform to numeric columns
        income_df_clean["GeoFips"] = income_df_clean["GeoFips"].apply(pd.to_numeric)
        income_df_clean["DataValue"] = income_df_clean["DataValue"].str.replace(",", "")
        income_df_clean["DataValue"] = income_df_clean["DataValue"].apply(
            lambda x: pd.to_numeric(x, errors="coerce")).astype("Int64")
        return income_df_clean
