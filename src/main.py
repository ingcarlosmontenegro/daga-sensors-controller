from config.settings import getConfig
from infrastructure.sensor_reader import SensorReader
from infrastructure.sqlite.sqlite_database import SQLiteDatabase
from infrastructure.http.flask.application import generateFlaskApplication

READERS_PORT = config.get('readers_port')
PORT = config.get('PORT_HTTP')

def generate_control_readers():
    sensor_readers = []
    databases = []
    for i_reader in range(len(READERS_PORT)):
        reader_name = 'reader{}'.format(i_reader)
        reader = SensorReader(reader_name, READERS_PORT[i_reader])
        sensor_readers.append(reader)

        databases.append(SQLiteDatabase(reader_name))
    return sensor_readers, databases

function_data = generate_control_readers()
app = generateFlaskApplication(function_data)

# Application initialization
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)



