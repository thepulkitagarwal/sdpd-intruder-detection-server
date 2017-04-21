import urllib
import urllib2
import json

import RPi.GPIO as GPIO
import time

def sendStatus(status,
		url="http://10.42.0.1:3000/status/set", 
		headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}):
	'''sends a status "0" or "1" to signify intruder detected or not detected'''
	data = json.dumps({
		'intruderDetected': status
	})
	request = urllib2.Request(url, data, headers)
	content = urllib2.urlopen(request)
	print content.read()
	content.close()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
while True:
	i = GPIO.input(11)
	if i == 0:
		print "No intruders", i
	elif i == 1:
		print "Intruder detected", i
	sendStatus(i)
	time.sleep(1)
