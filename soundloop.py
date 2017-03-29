#!usr/bin/env python
#coding=utf-8

import time
import os
import random
import pygame


# Set sound dir from current working dir.
sound_dir = "sounds"

# Time between calls in seconds.
min_time_between_calls = 5
max_time_between_calls = 300

# Random range for volume (.0 1)
randome_volume_max = 1
random_volume_min = .1


def playRandomSound(lastTimePlayed=0):

    target_file = getFiles()

    volume = setAudioSettings(target_file)


    print_countdown()
    os.system('clear')
    print_details(target_file, volume)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def setAudioSettings(target_file):
    pygame.mixer.init()
    pygame.mixer.music.load(target_file)
    volume = random.uniform(random_volume_min, randome_volume_max)
    pygame.mixer.music.set_volume(volume)
    return volume


def getFiles():
    target_dir = os.path.join(os.getcwd(), "%s" % sound_dir)
    fileList = os.listdir(target_dir)
    random_randrange = random.randrange(0, len(fileList))
    target_file = os.path.join(target_dir, fileList[random_randrange])
    return target_file


def print_details(target_file, volume):
    print("Playing File {} ".format(target_file))
    print("Volume {}".format(volume))


def print_countdown():
    randomeTime = random.randrange(min_time_between_calls, max_time_between_calls)
    print("Time until next call: ")
    countdown(randomeTime)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1




if __name__ == '__main__':


    while True:
        playRandomSound()

