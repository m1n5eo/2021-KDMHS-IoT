import RPi.GPIO as GPIO

LED = [17, 27, 22]
SWITCH = [5, 6, 13]

GPIO.setmode(GPIO.BCM)
for i in range(3):
    GPIO.setup(LED[i], GPIO.OUT)
    GPIO.setup(SWITCH[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i in range(3):
            if(GPIO.input(SWITCH[i]) == 1):
                GPIO.output(LED[i], 1)
            else:
                GPIO.output(LED[i], 0)

finally:
    GPIO.cleanup()
    print('cleanup and exit')