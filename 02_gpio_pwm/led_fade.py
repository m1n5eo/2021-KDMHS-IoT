import RPi.GPIO as GPIO
import time

LED_PIN = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 50)       # PWM 인스턴스 생성 / 주파스 설정 : 50Hz
pwm.start(0)                      # duty cycle 0~100

try:
    for i in range(3):
        for j in range(0, 101, 5):        # 서서히 켜지게 하기
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
        for j in range(100, -1, -5):      # 서서히 꺼지게 하기
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)

finally:
    pwm.stop()      # PWM 종료
    GPIO.cleanup()
    print('cleanup and exit')