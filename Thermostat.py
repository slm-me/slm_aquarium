#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

#Define Relay outputs FAN - 18
FAN = 18
GPIO.setmode(GPIO.BCM)

# Setup GPIO pins
GPIO.setup(FAN, GPIO.OUT)

while True:
    # Open the file for the sensor and read contents
    tempfile = open("/sys/bus/w1/devices/28-021991777f63/w1_slave")
    thetext = tempfile.read()
    tempfile.close()
    # Get the temperature
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    # Print out the temperature
    print (temperature)
    
    
    if (temperature >= 25):
        GPIO.output(FAN, GPIO.LOW)
        print ("Fan is ON");

    else:
        GPIO.output(FAN, GPIO.HIGH)
        print ("Fan is OFF");

    time.sleep(600)
