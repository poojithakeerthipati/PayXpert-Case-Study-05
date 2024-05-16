import pyodbc
from Util.DBPropertyUtil import PropertyUtil
from MyExceptions import DataBaseConnectionException


class DBConnection:
    def __init__(self):
        try:
            conn_str = PropertyUtil.get_property_string()
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise DataBaseConnectionException("Sorry Error Happened😔")

    def close(self):
        self.cursor.close()
        self.conn.close()
