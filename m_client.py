import paho.mqtt.client as mqtt

app = Flask(__name__)
client = InfluxDBClient3(token="bI-T7PqS83eRNvS65L7ROctuc2JpO2iz0jEDd4BLo6wrKbLMsCrwl2rJK0i5XaRFXv0il42944I9aVif8K1Fhg==",
                        host="us-east-1-1.aws.cloud2.influxdata.com",
                        database="sensor_data",
                        org="SOE, CUSAT")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor_data")

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
          + message.topic + "' with QoS " + str(message.qos))
    try:
        data = message.payload.decode()
        sensor_data = {
            "sensorID": message.topic,
            "timestamp": data["timestamp"],
            "pH": float(data["pH"]),
            "temperature": float(data["temperature"]),
            "dissolved_oxygen": float(data["dissolved_oxygen"]),
            "turbidity": float(data["turbidity"]),
            "TDS": float(data["TDS"])
        }
        write_to_db(sensor_data)
    except Exception as e:
        print("Error processing message:", e)

def write_to_db(points):
    try:
        client.write(record=points, write_precision="s")

    except Exception as e:
        print("Error writing to InfluxDB:", e)

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"C1")
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("test.mosquitto.org", 1883, 60)
mqtt_client.loop_start()