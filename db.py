from influxdb_client_3 import InfluxDBClient3, flight_client_options
import certifi
import config
import pandas
import datetime
fh = open(certifi.where(), "r")
cert = fh.read()
fh.close()

client = InfluxDBClient3(token=config.Config.INFLUXDB_TOKEN,
                        host=config.Config.INFLUXDB_HOST,
                        database=config.Config.INFLUXDB_DATABASE,
                        org=config.Config.INFLUXDB_ORG,
                        flight_client_options=flight_client_options(
        tls_root_certs=cert))

def write_to_db(sensor_data):
    points = {
          "measurement": "data",
          "tags": {"sensor": sensor_data["sensorID"]},
          "fields": {"pH": sensor_data["pH"], "temp": sensor_data["temperature"], "tds":sensor_data["TDS"], "turb": sensor_data["turbidity"], "do": sensor_data["dissolved_oxygen"]},
          "time": datetime.datetime.now()
          }
    try:
        print(config.Config.INFLUXDB_HOST)
        client.write(record=points, write_precision="s")

    except Exception as e:
        print("Error writing to InfluxDB:", e)


def add_sensor(sensor):
    points = {
          "measurement": "s_list",
          "tags": {"sensor": sensor["sensorID"]},
          "fields": {"location": sensor["location"], "lat": sensor["lat"], "long":sensor["long"], "status": "online"},
          }
    try:
        print(config.Config.INFLUXDB_HOST)
        client.write(record=points, write_precision="s")

    except Exception as e:
        print("Error adding data", e)

def execute_chart_query():
    try:
        query = "SELECT * FROM data WHERE time >= now() - INTERVAL '30 days' ORDER BY time DESC LIMIT 12"
        pd = client.query(query=query, mode="pandas")
        reversed_data = pd.iloc[::-1].to_json(orient='records')
        return reversed_data

    except Exception as e:
        print("Error executing query:", e)
        return None
    

def get_analytics_data():
    try:
        query = "SELECT * FROM data WHERE time >= now() - INTERVAL '30 days' ORDER BY time"
        pd = client.query(query=query, mode="pandas")
        return pd

    except Exception as e:
        print("Error executing query:", e)
        return None
    
def get_download_data():
    try:
        query = "SELECT * FROM data ORDER BY time"
        pd = client.query(query=query, mode="pandas")
        return pd.to_json(orient='records')

    except Exception as e:
        print("Error executing query:", e)
        return None

def get_sensors():
    try:
        query = "SELECT * FROM s_list WHERE time>'2024-03-24T22:15:35.015Z' ORDER BY sensor"
        pd = client.query(query=query, mode="pandas")

        return pd.to_json(orient='records')

    except Exception as e:
        print("Error executing query:", e)
        return None