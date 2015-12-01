#!/usr/bin/python2
"""
    Copyright 2015 Steven Sheffey
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import time
import requests
import pickle
import Adafruit_DHT

with open("server.url","r") as server_url_file:
    server_url = server_url_file.read()


sensor = Adafruit_DHT.DHT22

pi_num = 1
pin = 11

while True:
    #Check if there is unsent data
    try:
        post_parameters = pickle.load(open("/tmp/unsent.pickle", "rb"))
    except:
        print("No unsent data file")
        post_parameters = []
    #Get data from temperature sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
        print 'Failed to get reading. Try again!'

    #Get time
    timestamp = int(time.time())


    post_parameters.append({'temperature':temperature, 'humidity':humidity, 'date_rec':timestamp, 'pi_num':pi_num})
    try:
        for data_point in post_parameter:
            requests.post(server_url, data=data_point)
            post_parameters.remove(data_point)
    except:
        print("POST request unsuccessful")
        e = sys.exc_info()[0]
        print(e)
    pickle.dump(post_parameters, open("/tmp/unsent.pickle", "wb"))
    time.sleep(10)
