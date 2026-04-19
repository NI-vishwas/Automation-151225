import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv() 

def get_conn():
    try:
        # connection = mysql.connector.connect(
        #     host="localhost",user="root",password="root",database="Northwind"
        # )
        db_user = os.getenv("DB_USER")
        db_pass = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_name = os.getenv("DB_NAME")


        engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}")
        return engine
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def get_table_data(table_name, engine):
    query = f"SELECT * FROM {table_name}"
    # df = pd.read_sql(query, connection)
    df = pd.read_sql(query, engine)
    return df

