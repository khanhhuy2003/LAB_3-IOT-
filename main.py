#!/usr/bin/env python3

import random
import sys
import time

from Adafruit_IO import MQTTClient
from uart import *
AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "khanhhuy03"
AIO_KEY = "aio_nAts10ednWcKaXGFeEYmWNt0qv3Y"


def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")


def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload)


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_ai = 5
while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        temp = random.randint(10, 30)
        client.publish("cambien1", temp)
        light = random.randint(10, 100)
        client.publish("cambien2", light)
        humidity = random.randint(10, 100)
        client.publish("cambien3", humidity)

    #counter_ai = counter_ai - 1

    # if counter_ai <= 0:
    #     counter = 5
    #     ai = detect_image()
    #     # print("AI output", ai)
    #     client.publish("ai", ai)
    # time.sleep(1)
    readSerial(client)
    time.sleep(1)
    pass
