from src.domain.sensor_data_reader_interface import SensorReaderInterface

class DatabaseInterface:
    def __init__(self,  sensor_reader_name: str):
        self._sensor_reader_name = sensor_reader_name

    def getReaderName(self):
        pass

    def addData(self, data: dict):
        pass

    def getData(self):
        pass

    def deleteReadData(self):
        pass
