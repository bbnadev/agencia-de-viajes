import mysql.connector
from database.config import db_config


class Database:
    def __init__(self):
        self.config = db_config

    def connect(self):
        return mysql.connector.connect(**self.config)

    def query(self, query, params=None):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        cursor.close()
        connection.close()

    def fetch(self, query, params=None):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def fetch_one(self, query, params=None):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result
