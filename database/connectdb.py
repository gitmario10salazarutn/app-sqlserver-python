# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:32 2023

@author: Mario
"""

import pymssql as conn
import psycopg2 as conn2
from decouple import config


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


def connect_sqlserver(hostname, dbname, username, password):
    try:
        # conexion = conn.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
        #                        hostname + ';DATABASE=' + dbname + ';UID=' + username + ';PWD=' + password)
        conexion = conn.connect(
            server=hostname, user=username, password=password, database=dbname)
        cursor = conexion.cursor()
        print("Database connect successfully to SQL Server")
        return cursor
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)


#print(connect_sqlserver("sql.bsite.net\MSSQL2016",
#      "mario10salazar_utn", "mario10salazar_utn", "2202113610Mario10"))


def get_connection():
    try:
        connection = connect_postgresql(
            config('HOST_NAME'),
            config('DATABASE'),
            config('USER_NAME'),
            config('PASSWORD')
        )
        return connection
    except Exception as ex:
        raise Exception(ex)


print(get_connection())
