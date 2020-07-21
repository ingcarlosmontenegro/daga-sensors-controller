import flask
from flask import Flask, jsonify
from config.settings import getConfig
from src.domain.database_interface import DatabaseInterface
from src.domain.sensor_reader_interface import SensorReaderInterface
from sensor_routes import defineSensorsRoutes

SENSOR_READERS = getConfig().get('readers_port')
ADDITIONAL_DATA = getConfig().get('additional_data')

# API Configuration
with open(ADDITIONAL_DATA) as additional_data:
    additional_data = json.load(err_msg)
    err_msg = additional_data.get('error_msg')
    sensor_properties = additional_data.get('sensor_properties')

# Handle Information
def addDataDB(databases: list, reader_name: str, data: dict):
    for db in databases:
        if db.getReaderName == reader_name:
            db.addData(data)

def readingNotification(reader: SensorReaderInterface, databases: list):
    read_data = reader.readSensors()
    if not isinstance(read_data, str):
        addDataDB(databases, reader.getName(), read_data)
    return read_data

def generateNotification(notif_msg: str, additional_info=None: dict):
    err_info = err_msg.get(notif_msg)
    measure_name = err_info.get('measure_name')
    description = err_info.get('description')
    if additional_info:
        measure_name = measure_name.format(additional_data.get('measure_name'))
        description = description.format(additional_data.get('description'))
    notification = {
        'controller_name': controller_name,
        'title_alert': err_info.get('title'),
        'measure_name': measure_name,
        'description': description,
        'is_hot': True
    }
    return notification

def verifySensorsState(sensor_data: dict):
    measure_name = ""
    description = ""
    data_keys = list(sensor_data.keys())
    for key in data_keys:
        if sensor_data.get(key) is 'None':
            measure_name += key + " "
            description += getSensorProperties(key) + " "
    additional_data = {
        "measure_name": measure_name,
        "description": description
    }
    if measure_name is not "":
        return generateNotification('sensor_failure', additional_data)
    return False

def getSensorProperties(sensor_name: str):
    for sensor in sensor_properties:
        if sensor.get('name') is sensor_name:
            return sensor.get('sensor_reference')

def notificationMessageError(read_data):
    notification = None
    if notif_name is 'no_connected':
        notification = generateNotification(read_data)
    else:
        notification = verifySensorsState(read_data)
    return notification

def comparisonLastNotification(notification, last_notification):
    #Comparison between notification



def generateFlaskApplication(readers: list, databases: list):
    app = Flask(__name__)
    last_notification = None
    while True:
        for reader in readers:
            read_data = readingNotification(reader, databases)
            notification = notificationMessageError(read_data)
            if  notification:
               if comparisonLastNotification(notification, last_notification)
            else if

        #assignement current_notification as last_notifcation
        last_notification = notification_list

    app.register_blueprint(defineSensorsRoutes(), url_prefix='/sensors')
    return app
