from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.mysql import MySQL
from pandas import DataFrame
from os import path
import time
import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2 
import io
import mysql.connector

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_mysql(fb_df, **kwargs) -> None:
    """
    Template for exporting data to a MySQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#mysql
    """

    conn_string = 'postgresql://admin:UkMDHIwlySKouoyDTYlk7gVo18mptjdR@dpg-cingqll9aq06u3gm6m80-a.ohio-postgres.render.com/social_collection'
    #perform to_sql test and print result
    db = create_engine(conn_string)
    conn = db.connect()   