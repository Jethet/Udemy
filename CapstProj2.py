# Alarm Clock:
# A simple clock where it plays a sound after X number of minutes/seconds or
# at a particular time.
# mp3 file is called Digital Alarm Sound
"""
import playsound
playsound.playsound('Digital_alarm_clock_sound.mp3')

def alarm(time):
    if time == 2:
        print('\a')

alarm(2)
"""

import pygame

pygame.mixer.init()
pygame.mixer.music.load('Digital_alarm_clock_sound.mp3')
pygame.mixer.music.play()

def alarm(time):
    if time == 2:
        print('\a')

alarm(2)
