from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

RED_LED = 4
BLUE_LED = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a><br>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == "red" and op == "on":
        GPIO.output(RED_LED, GPIO.HIGH)
        return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif color == "red" and op == "off":
        GPIO.output(RED_LED, GPIO.LOW)
        return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        '''
    elif color == "blue" and op == "on":
        GPIO.output(BLUE_LED, GPIO.HIGH)
        return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif color == "blue" and op == "off":
        GPIO.output(BLUE_LED, GPIO.LOW)
        return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()