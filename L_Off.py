#!/usr/bin/env python

import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
import time
import sys

pca.frequency = 100
led_channel = pca.channels[0]

for i in range(0xffff, 0, -1):
    led_channel.duty_cycle = i
    time.sleep(0.01);

sys.exit()
