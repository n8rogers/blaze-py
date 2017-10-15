#!/usr/bin/env python

import os, pygame
from time import sleep
from random import randint
import RPi.GPIO as GPIO

input1 = 26
input2 = 25
output1 = 21
item = 0

print "Initializing Mixer..."
pygame.mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setup(input1, GPIO.IN)
#GPIO.setup(input2, GPIO.IN)
GPIO.setup(output1, GPIO.OUT)

print "Ready..."
GPIO.output(output1, GPIO.HIGH)

soundsList = []
for file in os.listdir("."):
	if file.endswith(".mp3"):
		soundsList.append(file)

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
	print "Playing " + sound
	return sound

def playSound():
	pygame.mixer.music.load(getNextSound())
	pygame.mixer.music.play()


GPIO.setup(input1, GPIO.IN)
#GPIO.setup(input2, GPIO.IN)


while True:

    if (GPIO.input(input1)== False):
    	playSound()

    # if (GPIO.input(input2)== False):
    #     os.system('mpg123 -q blaze_theme.mp3')

    sleep(0.1);