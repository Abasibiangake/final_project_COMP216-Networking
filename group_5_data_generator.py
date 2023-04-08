import json
from random import randint
from time import asctime
from json import dumps
import random

class Util:
    def __init__(self, start_id=1):
        self.id = start_id
        self.temp = round(random.uniform(15, 25), 2)
        self.humid = round(random.uniform(30, 70), 2)
        self.aqi = round(random.uniform(50, 150), 0)

    def get_json_data(self):
        self.id += 1
        new_temp = round(random.uniform(self.temp - 1, self.temp + 1), 2)
        diff_temp = round(new_temp - self.temp, 2)
        self.temp = new_temp
        self.humid = round(random.uniform(self.humid - 5, self.humid + 5), 2)
        self.aqi = round(random.uniform(self.aqi - 10, self.aqi + 10), 0)
        data = {
            'id': self.id,
            'time': asctime(),
            'temperature': self.temp,
            'humidity': self.humid,
            'air_quality': self.aqi,
            'diff_temperature': diff_temp
        }
        return json.dumps(data)
    # data_nums=100;
    # y_data=[];
    # def __init__(self):
    #     self.start_id = 0
    #     self.temp = 0
    #     self.diff_temp = "-"
    #
    # def get_json_data(self):
    #     self.start_id += 1
    #     x = random.random()
    #     new_temp = round(10*x+15,2)
    #     if self.start_id>1: self.diff_temp= round(new_temp - self.temp,2)
    #     self.temp = new_temp
    #     humid = round(0.4+x/10,2)
    #     aqi = round(25+x*10,0)
    #     data = {'id': self.start_id, 'time': asctime(), 'temp': self.temp, 'humid': humid, 'AQI': aqi, "diff_temp": self.diff_temp}
    #     return dumps(data, indent=2)