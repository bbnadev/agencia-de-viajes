import mysql.connector
from mysql.connector import errorcode
from database.config import db_config


class Database:
    def __init__(self):
        self.config = db_config

    def checkDB(self):
        if self.connect():
            return True
        else:
            exit(1)

    def connect(self):
        try:
            return mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            match err.errno:
                case errorcode.ER_ACCESS_DENIED_ERROR:
                    print(
                        "(Database) Error en credenciales de acceso revisa el nombre y contraseña.")
                case errorcode.ER_BAD_DB_ERROR:
                    print("(Database) Base de datos no encontrada.")
                case _:
                    print(f"(Database) {err}")

    def query(self, query, params=None):
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print(
                f"(Database) Ocurrio un error al intentar ejecutar la query: {e}")

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
            print(
                f"(Database) Ocurrio un error al intentar ejecutar el fetch: {e}")

    def fetch_one(self, query, params=None):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result
