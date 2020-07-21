from src.domain.database_interface import DatabaseInterface

class GetDataSensor:
    def __init__(self, database: DatabaseInterface):
        self._db = database

    def execute(self, readers_id: int):
        return self._db.getDataReader(reader)

    
