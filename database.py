"""Provides methods to insert on database"""

import sqlite3
from tools import Tools
import json

DATABASE_FILE = "database.db"

class Database:
    """Exposes methods that interacts with database
    """
    def __init__(self):
        """Constructor. Defines instance variables
        """
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.conn.text_factory = str
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_table()
        self.tools = Tools()

    def create_table(self):
        """Creates the table in database"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ip (id INTEGER PRIMARY KEY, ip VARCHAR(100), mktime INTEGER(100), content VARCHAR(1000))")
        self.conn.commit()

    def insert_ip(self, ip, headers):
        """Inserts ip on ip table

        Args:
            ip  (str): ip address
            headers (str): headers from client 

        Returns:
            int: mktime of change
        """
        
        mktime = self.tools.get_time()
        response = "Already registered"
        sql_query = "SELECT ip FROM ip WHERE ip = '{}'".format(ip)
        query = self.cursor.execute(sql_query).fetchone()
        if query is None:
            sql_insert = "INSERT INTO ip (ip, mktime, content) VALUES ('{}', '{}', '{}')"
            self.cursor.execute(sql_insert.format(ip, mktime, headers))
            self.conn.commit()
            response = "Registered {}".format(mktime)
        return response

    def get_list_ip(self):
        """Get list of ip address with time from database
        """
        sql_query = "SELECT * FROM ip ORDER BY id"
        query = self.cursor.execute(sql_query)
        data = []
        if query:
            for field in query:
                data_dict = {"ip": field["ip"], "date": self.tools.get_iso_time(int(field["mktime"]))}
                data_dict.update(json.loads(field["content"]))
                data.append(data_dict)
        return data