#!/usr/bin/python3
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

import time
import requests
import pickle

data_url = ""

while True:
    #Check if there is unsent data
    try:
        post_parameters = pickle.load(open("/tmp/unsent.pickle", "rb")
    except:
        print("No unsent data file")
        post_parameters = []
    #Get data from temperature sensor
    temperature = 0
    humidity = 0
    #Get time
    timestamp = int(time.time())
    #Pi ID
    pi_id = 1
    
    post_parameters.append() = {'temperature':temperature, 'humidity':humidity, 'timestamp':timestamp, 'pi_id':pi_id}
    try:
        for index in range(len(post_parameters)):
            #requests.post(data_url, params=post_parameters[index])
            del post_parameters[index]
    except:
        print("Data saved to pickle file")
    pickle.dump(post_parameters, open("/tmp/unsent.pickle", "wb"))
