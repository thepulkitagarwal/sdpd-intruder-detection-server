import requests
import json

def sendStatus(status,
		url="http://10.2.2.14:3000/status/set", 
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}):
	'''sends a status "0" or "1" to signify intruder detected or not detected'''
	data = {
		'intruderDetected': status
	}
	response = requests.post(url, headers=headers, data=json.dumps(data))
	print response.content

sendStatus(1)
