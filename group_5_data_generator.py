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

    def get_json_data(self):
        self.start_id += 1
        x = random.random()
        temp = round(10*x+15,2)
        humid = round(0.4+x/10,2)
        aqi = round(25+x*10,0)
        data = {'id': self.start_id, 'time': asctime(), 'temp': temp, 'humid': humid, 'AQI': aqi}
        return dumps(data, indent=2)