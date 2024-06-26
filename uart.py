import serial.tools.list_ports
import random
import time
import sys
from Adafruit_IO import MQTTClient

# def getPort():
#     ports = serial.tools.list_ports.comports()
#     commPort = "None"
#     for i in range(0, N):
#         port = ports[i]
#         strPort = str(port)
#         if "COM" in strPort:
#             splitPort = strPort.split(" ")
#             commPort = (splitPort[0])
#     return commPort
def getPort():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "COM" in port.description:
            return port.device
    return "None"

def processData(client,data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("cambien1", splitData[2])
    if splitData[1] == "A":
        client.publish("cambien2", splitData[2])

ser = serial.Serial(port=getPort(), baudrate=115200)
print(ser)
mess = ""
def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]
def writeData(data):
    ser.write(str(data).encode('utf-8'))