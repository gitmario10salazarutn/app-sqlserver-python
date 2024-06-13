# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:32 2023

@author: Mario
"""

import psycopg2 as conn2
from decouple import config
import pymssql


def connect_postgresql(hostname, dbname, username, password):
    try:
        conn_post = conn2.connect(
        dbname=dbname,
        user=username,
        password=password,
        host=hostname,
        port=5432)
        return conn_post
    except Exception as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
        raise Exception(e)

"""
def connect_sqlserver1(hostname, dbname, username, password):
    try:
        #connectionString = f'DRIVER={{SQL 17 Server}};SERVER={hostname};DATABASE={dbname};UID={username};PWD={password}'
        connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={hostname};DATABASE={dbname};UID={username};PWD={password}'
        conn = pyodbc.connect(connectionString)
        cursor = conn.cursor()
        #print("Database connect successfully to SQL Server")
        return conn
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
"""
# KskN2u7bPpz*aZd 
def connect_sqlserver(hostname, dbname, username, password):
    try:
        #print(hostname, dbname, username, password, config('HOST_NAMESQL'))
        conn = pymssql.connect(
    server=hostname,
    user=username,
    password=password,
    database=dbname,
    as_dict=True
) 
        #cursor = conn.cursor()
        return conn
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)

 


def get_connection():
    try:
        connection = connect_sqlserver(
            'SQL8006.site4now.net',
            'db_aa9d6d_marioutn',
            'db_aa9d6d_marioutn_admin',
            'KskN2u7bPpz*aZd'
        )
        return connection
    except Exception as ex:
        raise Exception(ex)
