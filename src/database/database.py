import mysql.connector
from mysql.connector import Error
from database.config import db_config


class Database:
    def __init__(self):
        self.config = db_config

    def connect(self):
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print(
                f"Ocurrio un error al intentar conectarse a la base de datos: {e}")

    def query(self, query, params=None):
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Ocurrio un error al intentar ejecutar la query: {e}")

    def fetch(self, query, params=None):
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print(f"Ocurrio un error al intentar ejecutar la query: {e}")

    def fetch_one(self, query, params=None):
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print(f"Ocurrio un error al intentar ejecutar la query: {e}")
