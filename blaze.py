#!/usr/bin/env python

import os, pygame
from time import sleep
from random import randint

pygame.mixer.init()

import RPi.GPIO as GPIO

input1 = 26
input2 = 25
item = 0
playing = False

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
	if(playing):
		pygame.mixer.stop()
		playing = False
	else:
		pygame.mixer.music.load(getNextSound())
		pygame.mixer.music.play()
		playing = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(input1, GPIO.IN)
#GPIO.setup(input2, GPIO.IN)


while True:

    if (GPIO.input(input1)== False):
    	playSound()

    # if (GPIO.input(input2)== False):
    #     os.system('mpg123 -q blaze_theme.mp3')

    sleep(0.1);