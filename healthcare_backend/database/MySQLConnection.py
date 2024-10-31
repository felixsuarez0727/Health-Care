import mysql.connector
from mysql.connector import Error

class MySQLConnection:
    _instance = None

    def __new__(cls):       
        if cls._instance is None:
            try:
                cls._instance = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="2802",
                    database="db_healthcare"
                )
                print("Conexión a MySQL establecida.")
            except Error as e:
                print(f"Error al conectar a MySQL: {e}")
                cls._instance = None
        return cls._instance

    @classmethod
    def get_connection(cls):
        """Retornar la instancia existente o crear una nueva si no existe"""
        if cls._instance is None:
            cls()
        return cls._instance