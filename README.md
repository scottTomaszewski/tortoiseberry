tortoiseberry
=============

Tortoise tank sensor visualization and management via a raspberry pi

![alt tag](https://raw.github.com/scottTomaszewski/tortoiseberry/master/images/tortoiseberry.png)

Features

* DHT Sensors in 4 corners of the the tank for temperature and humidity
* Status of overhead and basking light
* Ability to toggle lights manually or on a schedule (apscheduler)
* Time and date
* Current weather, temperature outside, and high/low for the day (openWeatherMap.org)
* Auto updates page (sensors, light status, weather) without page reload every 5 seconds

Components

* Raspberry pi model B
* 4x DHT11 Sensors (to be upgraded to DHT22 for accuracy)
* 8 Channel Relay Module

Setup
=====

    git clone git@github.com:scottTomaszewski/tortoiseberry.git

**_External Requirements_**

**APScheduler** - http://pythonhosted.org/APScheduler/#installing-apscheduler

Reliable scheduling in python

    pip install apscheduler

**pigpio** - http://abyz.co.uk/rpi/pigpio/index.html

Library for interacting with gpio pins on the raspberry pi in python

    wget abyz.co.uk/rpi/pigpio/pigpio.zip
    unzip pigpio.zip
    cd PIGPIO
    make
    make install

Running
=======

Startup pigpio

    sudo pigpiod

Start the server

    sudo python Server.py

Browse to site at localhost:3674

To get the data from the server in json, make a GET request to localhost:3674/update


TODO
====

(In no particular order)

* Use javascript + json to send the light toggling request
* Convert the weather into a double size container to give room for
  * 4-day forcast
  * Wind
  * Chance of precipitation (maybe throughout the day similar to google weather)
  * Units of measurement for temperatures
  * Temperature throughout the day
* Webcam
* Config options for
  * Weather location
  * DHT sensor ports
  * Relay channel ports
  * Color options
  * Celcius vs Fahrenheit
  * Range used for temperature and humidity
* Mobile support 
* Power-user mode
  * Graphs of sensor output over time
* Authentication for sensor input (light toggling)
