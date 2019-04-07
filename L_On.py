#!/usr/bin/env python

import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
import time
import sys

dt = list(time.localtime())
hour = dt[3]
minute = dt[4]
second = dt[5]
time.sleep(1)
print (hour, ":", minute, ":", second);

pca.frequency = 100
led_channel = pca.channels[0]

if (hour >= 8 and hour < 22):
    for i in range(0xffff):
        led_channel.duty_cycle = i;

else:
    led_channel.duty_cycle = 0;

sys.exit()
