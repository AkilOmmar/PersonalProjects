#! /uusr/lib/python2.7
import RPi.GPIO as GPIO
import time
PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
while True:
	GPIO.output(PIN, True)
	time.sleep(2)
	print 'LED OFF'
	GPIO.output(PIN, False)
	time.sleep(2)
	print 'LED ON'
	
