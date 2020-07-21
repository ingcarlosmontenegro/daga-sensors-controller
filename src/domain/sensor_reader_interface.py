class SensorReaderInterface:
    def __init__(self, reader_name: str, port: str):
        self.reader_name = reader_name
        self.port = port

    def getName(self):
        pass

    def configSensor(self):
        pass

    def readSensors(self):
        pass
