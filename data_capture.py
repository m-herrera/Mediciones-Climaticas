from time import sleep
import serial
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid
from datetime import datetime

auth = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(['192.168.199.129'], auth_provider=auth)
session = cluster.connect()
session.execute('USE Clima;')

ser = serial.Serial('COM3', 9600)  # Establish the connection on a specific port
while True:
    try:
        str_data = str(ser.readline()).lstrip("b").strip("'").rstrip("\\r\\n")
        data = str_data.split(",")  # Read the newest output from the Arduino
        rows = session.execute(
                    'INSERT INTO Medicion (IdMedicion, Temperatura, Humedad, Instante) VALUES (%s, %s, %s, %s)',
                    (uuid.uuid1(), float(data[1]), float(data[0]), datetime.now()))

    except Exception as e:
        print(e)