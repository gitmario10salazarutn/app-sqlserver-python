# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:32 2023

@author: Mario
"""

from decouple import config
import pymssql


def connect_sqlserver(hostname, dbname, username, password):
    try:
        # print(hostname, dbname, username, password, config('HOST_NAMESQL'))
        conn = pymssql.connect(
            server=hostname,
            user=username,
            password=password,
            database=dbname,
            as_dict=True
        )
        # cursor = conn.cursor()
        return conn
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)


def get_connection():
    try:
        connection = connect_sqlserver(
            config("HOSTNAME_SQLSERVER_AWS"),
            config("DATABASE_SQLSERVER_AWS"),
            config("USERNAME_SQLSERVER_AWS"),
            config("PASSWORD_SQLSERVER_AWS")
        )
        return connection
    except Exception as ex:
        raise Exception(ex)
