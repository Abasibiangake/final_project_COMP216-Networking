import tkinter

import paho.mqtt.client as mqtt
from time import sleep
from group_5_data_generator import Util
import random

class publisher:
    def __init__(self, delay=5, topic='COMP216', failure_rate=1):
        self.gen = Util()
        self.client = mqtt.Client()
        self.topic = topic
        self.delay = delay
        self.failure_rate = failure_rate

    def publish(self, times=150):
        self.client.connect('localhost', 1883)
        for x in range(times):
            print(f'#{x}', end=' ')

            if random.randint(0, 99) < self.failure_rate:
                print('Transmission failed')
                sleep(self.delay)  # Wait for some time before retrying
                continue
            data = self.gen.get_json_data()
            print(f'{data} to broker')
            try:
                self.client.publish(self.topic, payload=data)
            except Exception as e:
                print(f'Error publishing message: {e}')
                sleep(self.delay)  # Wait for some time before retrying
        self.client.disconnect()

    # def publish(self, times=10):
    #     for x in range(times):
    #         print(f'#{x}', end=' ' )
    #         self.__publish()

    # def __publish(self):
    #     data = self.gen.get_json_data()
    #     print(f'{data} to broker')
    #     self.client.connect('localhost', 1883)
    #     self.client.publish(self.topic, payload=data)
    #     sleep(self.delay)                           #necessary
    #     self.client.disconnect()



pub = publisher()
pub.publish()
