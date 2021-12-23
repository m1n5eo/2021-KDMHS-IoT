from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

RED_LED_PIN = 21
BLUE_LED_PIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == "red" and op == "on":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        return "RED LED ON"
    elif color == "red" and op == "off":
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        return "RED LED OFF"
    elif color == "blue" and op == "on":
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
        return "BLUE LED ON"
    elif color == "blue" and op == "off":
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)
        return "BLUE LED OFF"
    else:
        return "Error"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()