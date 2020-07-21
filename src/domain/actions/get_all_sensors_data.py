 class GetAllSensorsData:
     def __init__(self, databases: list):
         self._databases = databases

    def execute(self):
        sensors_data = {}
        for db in self._databases:
            sensor_name = db.getReaderName()
            sensor_data[sensor_name] = db.getData()
            db.deleteReadData()
        return sensor_data

