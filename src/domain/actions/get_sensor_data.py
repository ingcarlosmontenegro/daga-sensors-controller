from src.domain.database_interface import DatabaseInterface

class GetDataSensor:
    def __init__(self, database: DatabaseInterface):
        self._db = database

    def execute(self):
        return self._db.getData()
