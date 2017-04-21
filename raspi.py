import urllib
import urllib2
import json

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

sendStatus(1)
