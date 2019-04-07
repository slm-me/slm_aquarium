# slm_aquarium

Raspberry Pi Aquarium 

Install PCA9685 and ServoKit Libraries:

sudo pip3 install adafruit-circuitpython-pca9685

sudo pip3 install adafruit-circuitpython-servokit

Put it in the folder /home/pi/Documents/

Install Task Schedule: sudo apt-get install gnome-schedule

Edit crontab:

Relay - start at reboot

Thermostat - start at reboot

L_On - start at reboot

L_Off - start at 21:59

Reboot - 8:00 everyday
