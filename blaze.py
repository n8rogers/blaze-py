#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO.setup(23, GPIO.IN)
# GPIO.setup(24, GPIO.IN)
GPIO.setup(26, GPIO.IN)

sound

while True:
    # if (GPIO.input(23) == False):
    #     os.system('mpg123 -q binary-language-moisture-evaporators.mp3 &')

    # if (GPIO.input(24) == False):
    #     os.system('mpg123 -q power-converters.mp3 &')

    if (GPIO.input(26)== False):
        os.system('mpg123 -q blaze_theme.mp3')

    sleep(0.1);