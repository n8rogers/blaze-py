#!/usr/bin/env python
import logging

logging.basicConfig(filename='/home/pi/Github/blaze-py/blaze.out', level=logging.INFO)
logging.info("Initializing Mixer...")

import os, pygame, atexit
from time import sleep
from random import randint
import RPi.GPIO as GPIO

input1 = 26
input2 = 25
output1 = 21
item = 0

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setup(input1, GPIO.IN)
#GPIO.setup(input2, GPIO.IN)
GPIO.setup(output1, GPIO.OUT)

logging.info("Ready...")
GPIO.output(output1, GPIO.HIGH)

soundsList = []
directory = "/home/pi/Github/blaze-py/"
for file in os.listdir(directory):
	if file.endswith(".mp3"):
		soundsList.append(directory + file)

@atexit.register
def goodbye():
	logging.info("Exiting")
	GPIO.cleanup()

def getRandomSound():
	listSize = len(soundsList)
	if(listSize > 0):
		return soundsList[randint(0,listSize-1)]
	else:
		return null


def getNextSound():
	global item 
	item += 1
	if(item > len(soundsList) - 1):
		item = 0;
	sound = soundsList[item]
	logging.info("Playing " + sound)
	return sound

def playSound():
	pygame.mixer.music.load(getNextSound())
	pygame.mixer.music.play()


GPIO.setup(input1, GPIO.IN)
#GPIO.setup(input2, GPIO.IN)

rec = True
while True:
	push = (GPIO.input(input1) == False
    if (push):
    	if (rec):
    		playSound()
    		rec = False
    else:
    	rec = True

    sleep(0.1);