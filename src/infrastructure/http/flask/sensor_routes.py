from flask import Blueprint, request, make_response, jsonify
from src.domain.actions.get_all_sensors_data import GetAllSensorsData

def defineSensorsRoutes(getAllData: GetAllSensorsData):
    sensors_bp = Blueprint('sensor_bp', __name__)

    @sensors_bp.route('/sensors_data', methods = ['POST'])
    def getSensorsData():
        return jsonfy(getAllData.execute())
    return sensors_bp
