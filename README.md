tortoiseberry
=============

Tortoise tank sensor management via a raspberry pi

    git clone git@github.com:scottTomaszewski/tortoiseberry.git
    cd tortoiseberry
    git submodule update --init

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
