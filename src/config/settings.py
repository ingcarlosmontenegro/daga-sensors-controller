import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv()

_config = {
    'control_name': os.getenv("CONTROLLER_NAME"),
    'readers_port': os.getenv("READERS_PORT").split(','),
    'sensor_reader_range': os.getenv("SENSOR_READER_RANGE"),
    'port_http': os.getenv("PORT_HTTP"),
    'sqlt_path': os.getenv("SQLT_DB_PATH")
    'additional_data': os.getenv("ADDITIONAL_DATA_PATH")
}

def getConfig():
    return _config
