import sqlite3
from src.config.settings import getConfig

DB_PATH = getConfig().get('SQLITE_DB_PATH')

class Connection:
    def __init__(self, db_name):
        self.db_name = db_name
        try:
            db_dir = '{}db{}.db'.format(DB_PATH, self.db_name)
            self.connection = sqlite3.connect(db_dir, check_same_thread = False)
            self.cursor = self.connection.cursor()
            print('DB: Database Conected')
        except sqlite3.OperationalError as error:
            print('Error:', error)

    def createTable(self, params_table):
        try:
            params = ''
            for prop in params_table:
                if params_table[0] is not prop:
                    params += ', '
                params += prop + ' TEXT'
            query = """CREATE TABLE
            IF NOT EXISTS {}({});
            """.format(self.db_name, params)
            self.cursor.execute(query)
            print('DB: Users Table created')
        except sqlite3.OperationalError as error:
            print('DB Error:', error)

    def getConnectionProps(self):
        return self.connection, self.cursor

    def closeConnection():
        self.connection.close()
        print('DB: OFFLINE DataBase')
