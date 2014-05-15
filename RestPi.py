from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)
app.config.from_object('config')
GPIO.setmode(GPIO.BOARD)

@app.route("/")
def helloRestPi():
	return "Welcome to RestPi! A REST API for Raspberry Pi!" 
@app.route("/setInput")
def setInput():
	GPIO.setup(int(request.args.get('pin')), GPIO.IN)
	return request.args.get('pin') + " is Input!"

@app.route("/setOutput")
def setOutput():
        GPIO.setup(int(request.args.get('pin')), GPIO.OUT)
        return request.args.get('pin') + " is Output!"

@app.route("/readPin")
def readPin():
	value = GPIO.input(request.args.get('pin'))
	return "Pin value is" + value
@app.route("/writePin")
def writePin():
	GPIO.output(request.args.get('pin'), request.args.get('state'))
	return request.args.get('pin') + " is " + request.args.get('state') 

if __name__ == "__main__":
	app.run()
