import RPi.GPIO as GPIO
import time

LED_PIN = [17, 27, 22]

GPIO.setmode(GPIO.BCM)
for i in range(3):
    GPIO.setup(LED_PIN[i], GPIO.OUT)

for i in range(3):
    GPIO.output(LED_PIN[i], GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED_PIN[i], GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()      # GPIO 핀 상태 초기화
