from typing import Any

import pandas as pd

from common.transformer import Transformer


class CSVTransformer(Transformer):
    def transform(self, data) -> Any:
        # select only 2019 data
        poverty_df_2019 = data.loc[:, "Unnamed: 0":"Unnamed: 7"]
        # suppress unused header
        new_header = poverty_df_2019.iloc[0]
        poverty_df_2019 = poverty_df_2019[1:]
        poverty_df_2019.columns = new_header
        # suppress "County" from name column
        poverty_df_2019.Name = poverty_df_2019.Name.apply(lambda x: x.replace("County", "").strip())
        # suppress total per state as it is a duplication
        poverty_df_2019 = poverty_df_2019[poverty_df_2019["County FIPS code"] != "0"]
        # add geofips column
        poverty_df_2019["GeoFips"] = poverty_df_2019["State FIPS code"] + poverty_df_2019["County FIPS code"].str.zfill(
            3)
        # drop state and country fips
        poverty_df_2019.drop(["State FIPS code", "County FIPS code"], axis=1, inplace=True)
        # transform columns to numeric
        numeric_columns = poverty_df_2019.columns.drop(["Name", "State Postal Code"])
        poverty_df_2019[numeric_columns] = poverty_df_2019[numeric_columns].apply(pd.to_numeric).astype("Int64")
        # column order
        poverty_df_2019 = poverty_df_2019[
            ["GeoFips", "Name", "State Postal Code", "Poverty Universe, All Ages", "Poverty Universe, Age 5-17 related",
             "Poverty Universe, Age 0-17", "Poverty Universe, Age 0-4"]]
        return poverty_df_2019
