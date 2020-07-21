# -*- coding: utf-8 -*-
import sqlite3
from src.domain.database_interface import DatabaseInterface
from sqlite_connection import Connection

class SQLiteDatabase(DatabaseInterface):
    def __init__(self, sensor_reader_name):
        self.table_name = self.sensor_reader_name
        self.connection = Connection(sensor_reader.getName())
        self.conn, self.cursor = self.connection.getConnectionProps()

    def getReaderName(self):
        return self.sensor_reader_name

    def addData(self, data):
        query = 'INSERT INTO ' + self.sensor_reader_name + "("
        data_query = []
        pos_data = ''
        attrib = list(data.keys())
        for a in attrib:
            if a != attrib[-1]:
                query += a +", "
                pos_data += '?,'
            else:
                pos_data+= '?)'
                query += a + ") VALUES(" + pos_data
            data_query.append(data.get(a))

        try:
            self.cursor.execute(query, data_query)
            self.conn.commit()
            print('Database: New data added')
            return True
        except sqlite3.OperationalError as error:
            print(error)
            return False

    def getData(self):
        objs = []
        try:
            query = "SELECT * FROM "+ self.sensor_reader_name +";"
            self.cursor.execute(query)
            objs_query = self.cursor.fetchall()
            for reg in objs_query:
                objs.append(reg)
        except sqlite3.OperationalError as error:
            print("TB Error:", error)
        return objs

    def deleteReadData(self):
        query = "DELETE FROM " + self.sensor_reader_name + ";"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Database: Data deleted")
            return True
        except sqlite3.OperationalError as error:
            print("TB Error:", error)
            return False
