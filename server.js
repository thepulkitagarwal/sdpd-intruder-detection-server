var express = require('express')
var app = express()
var server = require('http').createServer(app)
var bodyParser = require('body-parser')
app.use(bodyParser.json())

var intruderDetected = false

app.get('/status/intruderDetected', function(req, res) {
	if(intruderDetected) {
		res.send('1')
	}
	else {
		res.send('0')
	}
})

app.post('/status/set', function(req, res) {
	console.log('Received intruderDetected status "' + req.body.intruderDetected + '" from ' + req.ip)

	var sendstr = ''
	if(req.body.intruderDetected == 1 || req.body.intruderDetected == 0) {
		intruderDetected = !!req.body.intruderDetected
		console.log('Setting intruderDetected = ' + intruderDetected)
		sendstr = 'OK.'
	}
	else {
		sendstr = 'Failed!'
	}

	res.send(sendstr + ' Received: ' + req.body.intruderDetected)
})

app.use(function (req, res, next) {
	res.status(404).send('404')
})

server.listen(3000, function() {
	console.log('Listening on http://' + require('os').networkInterfaces().eth0[0].address + ':3000')
});

