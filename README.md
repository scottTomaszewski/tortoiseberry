tortoiseberry
=============

Tortoise tank sensor management via a raspberry pi

![alt tag](https://raw.github.com/scottTomaszewski/tortoiseberry/master/images/tortoiseberry.png)

Setup
=====

    git clone git@github.com:scottTomaszewski/tortoiseberry.git

External Requirements 

APScheduler - http://pythonhosted.org/APScheduler/#installing-apscheduler
Reliable scheduling in python

    pip install apscheduler

pigpio - http://abyz.co.uk/rpi/pigpio/index.html
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
