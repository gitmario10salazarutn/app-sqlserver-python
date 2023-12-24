# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:32 2023

@author: Mario
"""

import pyodbc
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
        #connectionString = f'DRIVER={{SQL 17 Server}};SERVER={hostname};DATABASE={dbname};UID={username};PWD={password}'
        connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={hostname};DATABASE={dbname};UID={username};PWD={password}'
        conn = pyodbc.connect(connectionString)
        cursor = conn.cursor()
        print("Database connect successfully to SQL Server")
        cursor.execute('select*from users;')
        # Obtener los resultados
        rows = cursor.fetchall()
        # Imprimir los resultados
        for row in rows:
                #lista_users.append(row)
            print(row)
        return conn
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)

print("Mario Salazar", config('HOST_NAME'))


print("Mario Salazar", config('HOST_NAME'))

def get_connection():
    try:
        connection = connect_sqlserver(
            config('HOST_NAME'),
            config('DATABASE'),
            config('USER_NAME'),
            config('PASSWORD')
        )
        return connection
    except Exception as ex:
        raise Exception(ex)


print(get_connection())
