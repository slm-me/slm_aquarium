#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

#Define Relay outputs R1-Lights, R2-Compressor, R3-UV
R1 = 22
R2 = 27
R3 = 17

GPIO.setmode(GPIO.BCM)

# Setup GPIO pins
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)

while True:
        
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
    second = dt[5]
    time.sleep(1)
    print (hour, ":", minute, ":", second);
    
    if (hour >= 0 and hour < 8):
        GPIO.output(R1, GPIO.HIGH)
        GPIO.output(R2, GPIO.HIGH)
        GPIO.output(R3, GPIO.HIGH)
        print ("Lights are OFF, Compressor is OFF, UV is OFF");
        
    if (hour >= 8 and hour < 22):
        GPIO.output(R1, GPIO.LOW)
        GPIO.output(R2, GPIO.HIGH)
        GPIO.output(R3, GPIO.HIGH)
        print ("Lights are ON, Compressor is OFF, UV is OFF");
       		
    if (hour >= 22 and hour < 24):
        GPIO.output(R1, GPIO.HIGH)
        GPIO.output(R2, GPIO.LOW)
        GPIO.output(R3, GPIO.HIGH)
        print ("Lights are OFF Compressor is ON, UV is OFF");
