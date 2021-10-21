#!/usr/bin/env python

import time

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)

time.sleep(0.25)

GPIO.output(22, GPIO.HIGH)
GPIO.cleanup()
