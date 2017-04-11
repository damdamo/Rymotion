#! /usr/bin/env python3

import time
import pygame
from pygame.locals import *
import sys

def import_beats(beats_file):
    tempo = []
    with open(beats_file) as beats:
        for beat in beats:
            #lol = round(int(beat.split())[0])
            tic = round(float((beat.split())[0]), 5)
            tempo.append(tic)
    return tempo

#Initialisation
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
#pygame.init()
son = pygame.mixer.Sound("shadows.wav")
sonWood = pygame.mixer.Sound("wood.wav")

beats_file = "beat.txt"

tempo = import_beats(beats_file)
print(tempo)


error1 = time.clock()
son.play()
error2 = time.clock()
start_time = time.clock() + (error2- error1)

while 1:

    current_time = round((time.clock() - start_time), 5)
    #print(current_time, end = "")
    #sys.stdout.write('\r')

    if current_time in tempo:
        sonWood.play()
        print(current_time)
