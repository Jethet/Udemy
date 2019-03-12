# Alarm Clock:
# A simple clock where it plays a sound after X number of minutes/seconds or
# at a particular time.
# mp3 file is called Digital Alarm Sound

from playsound import playsound

def alarm(time):
    if time == 2:
        playsound()

alarm(2)
