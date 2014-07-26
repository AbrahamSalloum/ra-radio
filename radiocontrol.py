import RPi.GPIO as GPIO
import os
os.system("mpc clear")
os.system("mpc load listen.m3u")
os.system("mpc play")
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
        if(GPIO.input(24) == 0):
                os.system("shutdown -h now")
        if(GPIO.input(23) == 0):
                os.system("mpc prev")
                print("PREV")
        if(GPIO.input(22) == 0):
                os.system("mpc next")
                print("NEXT")
GPIO.cleanup()

