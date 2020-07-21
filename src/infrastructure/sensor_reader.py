import serial
import time
import json
import datetime as dt
from src.domain.sensor_reader_interface import SensoreReaderInterface
from config.settings import getConfig

READING_RANGE = int(getConfig().get('sensor_reader_range'))

class SensorReader(SensorReaderInterface):
    def __init__(self, reader_name, port):
        self.reader_name = reader_name
        self.port = port
        self.configSensor()

    def getName(self):
        return self.reader_name

    def configSensor(self):
        self._con = serial.Serial(self.port, 9600)
        self._reading_range = READING_RANGE

    def getDataSensors(self):
        jsonResult = None
        try:
            if not self._con.isOpen():
                self._con.open()
            jsonResult = self._con.readline()
        except serial.serialutil.SerialException as err:
            print('Error -> ', err)
            self._con.close()
        return jsonResult

    def readSensors(self):
        sensor_data = self.getDataSensors()
        state_data = 'caliper'
        if sensor_data:
            try:
                state_data = json.loads(sensor_data)
                state_data['time'] = dt.datetime.now()
            except ValueError:
                pass
        else:
            state_data = 'no_connected'
        time.sleep(self._reading_range)
        return state_data

