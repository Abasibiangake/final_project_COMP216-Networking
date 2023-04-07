from random import randint
from time import asctime
from json import dumps
import random
import calendar
import time

class Util:
    data_nums=100;
    y_data=[];
    def __init__(self):
        self.start_id = 0
        self.temp = 0
        self.diff_temp = "-"

    def get_json_data(self):
        self.start_id += 1
        x = random.random()
        new_temp = round(10*x+15,2)
        if self.start_id>1: self.diff_temp= round(new_temp - self.temp,2)
        self.temp = new_temp
        humid = round(0.4+x/10,2)
        aqi = round(25+x*10,0)
        data = {'id': self.start_id, 'time': asctime(), 'temp': self.temp, 'humid': humid, 'AQI': aqi, "diff_temp": self.diff_temp}
        return dumps(data, indent=2)