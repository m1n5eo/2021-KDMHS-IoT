import RPi.GPIO as GPIO
import time

BUZZER_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
song = [4, 4, 5, 5, 4, 4, 2, 4, 4, 2, 2, 1, 4, 4, 5, 5, 4, 4, 2, 4, 3, 2, 3, 0]
arr = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1.5,
       0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 2.5]

try:
    for i in song:
        pwm.ChangeFrequency(melody[i])
        time.sleep(arr[i])
finally:
    pwm.stop()
    GPIO.cleanup()