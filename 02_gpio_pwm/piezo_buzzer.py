import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
song = [0, 1, 2, 3, 4, 5, 6, 7, 8]

try:
    for i in song:
        pwm.ChangeFrequency(melody[i])
        time.sleep(1)
finally:
    pwm.stop()
    GPIO.cleanup()