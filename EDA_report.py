import sys
import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy import text
#from sqlalchemy.dialects.mysql import pymysql
import pandas as pd
import sweetviz as sv
import sqlite3
import numpy
import argparse
import pathlib
import configparser
import IPython

parser = argparse.ArgumentParser(description='Example argument parser')
parser.add_argument('--metadata_file', help='Path to the metadata CSV file', required=True, type=str)
args = parser.parse_args()
metadata_file = args.metadata_file
df_metadata = pd.read_csv(metadata_file)
print(df_metadata)
#following code passing the parameter through parameter.ini file
config_object = configparser.ConfigParser()
with open("parameter.ini","r") as file_object:
    config_object.read_file(file_object)
    source_type=config_object.get("Source","source_type")
    source_jdbc=config_object.get("Source", "source_jdbc")
    source_url=config_object.get("Source", "source_url")
    source_username=config_object.get("Source", "source_username")
    source_password=config_object.get("Source", "source_password")
    source_port=config_object.get("Source", "source_port")
    source_db=config_object.get("Source", "source_db")
    source_schema=config_object.get("Source", "source_schema")
    source_table=config_object.get("Source", "source_table")

    #metadata_file=config_object.get("Meatada-file", "metadata_file")

    target_type=config_object.get("Target", "target_type")
    target_jdbc=config_object.get("Target", "target_jdbc")
    target_url=config_object.get("Target", "target_url")
    target_username=config_object.get("Target", "target_username")
    target_password=config_object.get("Target", "target_password")
    target_port=config_object.get("Target", "target_port")
    target_db=config_object.get("Target", "target_db")
    target_schema=config_object.get("Target", "target_schema")
    target_table=config_object.get("Target", "target_table")

    print(source_type)
    print(target_type)
    # Access the metadata columns which contain Y flags
    df_metadata_source = df_metadata.loc[ ((df_metadata['FLAGS'] == 'Y') & (df_metadata['SOURCE_TYPE'] == source_type)), 'SOURCE_COLUMN'].values
    df_metadata_target = df_metadata.loc[ ((df_metadata['FLAGS'] == 'Y') & (df_metadata['TARGET_TYPE'] == target_type)), 'TARGET_COLUMN'].values

    str1 = (",".join(df_metadata_source))
    str2 = (",".join(df_metadata_target))

    print(str1)
    print(str2)

    sjdbc = source_jdbc + '://' + source_username + ':' + source_password + '@' + source_url + '/'
    tjdbc = target_jdbc + '://' + target_username + ':' + target_password + '@' + target_url + '/'
    print(tjdbc)
    print(sjdbc)

    engine = sqlalchemy.create_engine(sjdbc)
    with engine.connect() as connection:
        if (source_type == 'MySql'):
            result1 = connection.execute(text("SELECT {} FROM {}.{}".format(str1, source_db, source_table)))
            # print(result1)
            df1 = result1.fetchall()
            df1 = pd.DataFrame(df1, columns=[column for column in result1.keys()])
        else:
            result1 = connection.execute(
                text("SELECT {} FROM {}.{}.{}".format(str1, source_db, source_schema, source_table)))
            # print(result1)
            df1 = result1.fetchall()
            df1 = pd.DataFrame(df1, columns=[column for column in result1.keys()])

    # Read the record count of each table in the target database
    engine = sqlalchemy.create_engine(tjdbc)
    with engine.connect() as connection:
        if (target_type == 'MySql'):
            result1 = connection.execute(text("SELECT {} FROM {}.{}".format(str2, target_db, target_table)))
            # print(result1)
            df2 = result1.fetchall()
            df2 = pd.DataFrame(df1, columns=[column for column in result1.keys()])
        else:
            result1 = connection.execute(
                text("SELECT {} FROM {}.{}.{}".format(str2, target_db, target_schema, target_table)))
            # print(result1)
            df2 = result1.fetchall()
            df2 = pd.DataFrame(df1, columns=[column for column in result1.keys()])

    print(df1)
    print(df2)
    # Perform EDA using Sweetviz
    report = sv.compare([df1, "Source"], [df2, "Target"])
    sv.config_parser.read("sweetviz_defaults.ini")
    report.show_html()
    # import sweetviz as sv
    #report.show_html('compare.html', open_browser=True)
    # displaying results
   # IPython.display.HTML('compare.html')
