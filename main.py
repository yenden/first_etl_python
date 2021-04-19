# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os

from poverty_income.api_extractor import APIExtractor
from poverty_income.api_transformer import APITransformer
from poverty_income.csv_extractor import CSVExtractor
from poverty_income.csv_transformer import CSVTransformer
import pandas as pd
import argparse

from poverty_income.sqlite3_loader import Sqlite3Loader


def pipeline(config):
    # extract data
    print("Extract csv ")
    poverty_df = CSVExtractor(config["data_sources"]["csv"]).extract()
    print("Extract api ")
    income_df = APIExtractor(config["data_sources"]["api"]).extract()
    # transform data
    print("Transform csv ")
    poverty_transformed_df = CSVTransformer().transform(poverty_df)
    print("Transform api")
    income_transformed_df = APITransformer().transform(income_df)
    print("Transform all ")
    all_transform_df = pd.merge(poverty_transformed_df, income_transformed_df, on="GeoFips")
    # load data
    with Sqlite3Loader(config["data_sources"]["sqlite3"]) as db:
        db.load(all_transform_df, "etl_poverty_income")

    print("Loaded")


def parse_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Location of the config file", required=True)
    args = parser.parse_args()
    with open(args.config) as conf_file:
        config = json.load(conf_file)
    return config


def cli():
    config = parse_cmd_line_args()
    pipeline(config)
    print("over")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == "__main__":
    cli()
