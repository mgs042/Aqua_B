from flask import Flask, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import db
import config

app = Flask(__name__)
app.config.from_object(config.Config)
CORS(app)

@app.route('/', methods=['GET'])
def sensor_form():
    return render_template('sensor_form.html')

@app.route('/add_sensor', methods=['GET'])
def add_sensor_form():
    return render_template('add_sensor_form.html')

@app.route('/write', methods=['POST'])
def receive_sensor_data():
    try:
        sensor_data = {
            "sensorID": "S001",
            "timestamp": request.form.get('timestamp'),  
            "pH": float(request.form.get('pH')),
            "temperature": float(request.form.get('temperature')),
            "dissolved_oxygen": float(request.form.get('dissolved_oxygen')),
            "turbidity": float(request.form.get('turbidity')),
            "TDS": float(request.form.get('TDS'))
        }
        db.write_to_db(sensor_data)
        # Emit a message to the client to indicate that new data is available
        return "Data received and stored in InfluxDB"
    except Exception as e:
        print("Error processing request:", e)
        return "Error processing request", 500

@app.route('/new_sensor', methods=['POST'])
def create_new_sensor():
    try:
        sensor = {
            "sensorID": request.form.get('sensorId'),
            "lat": float(request.form.get('lat')),
            "long": float(request.form.get('long')),
            "location": request.form.get('location')
        }
        db.add_sensor(sensor)
        # Emit a message to the client to indicate that new data is available
        return "Data received and stored in InfluxDB"
    except Exception as e:
        print("Error processing request:", e)
        return "Error processing request", 500



@app.route('/chart_query',)
def chart_query():
    try:
        result = db.execute_chart_query()
        if result:
            return result
        else:
            return "Error processing request:"
    except Exception as e:
        print("Error processing request:", e)
        return "Error processing request", 500

@app.route('/list_sensor',)
def list_sensor():
    try:
        result = db.get_sensors()
        if result:
            return result
        else:
            return "Error processing request:"
    except Exception as e:
        print("Error processing request:", e)
        return "Error processing request", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
