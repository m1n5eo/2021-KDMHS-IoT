import RPi.GPIO as GPIO 
import time
from datetime import datetime # 모듈 불러오기

GPIO.setmode(GPIO.BCM)      # 초기 GPIO 설정

LedPIN = 14     # LED GPIO 핀번호
CdsPIN = 15     # CDS GPIO 핀번호
SwitchPIN = 5   # SWITCH GPIO 핀번호
PiezoPIN = 2    # Piezo buzzer GPIO 핀번호

segments = [11, 4, 23, 8, 7, 10, 18]    # segment GPIO 핀번호
digits = [22, 27, 17, 24]               # 4-digit FND GPIO 핀번호
data = [[1,1,1,1,1,1,0],    # 0
        [0,1,1,0,0,0,0],    # 1
        [1,1,0,1,1,0,1],    # 2
        [1,1,1,1,0,0,1],    # 3
        [0,1,1,0,0,1,1],    # 4
        [1,0,1,1,0,1,1],    # 5
        [1,0,1,1,1,1,1],    # 6
        [1,1,1,0,0,0,0],    # 7
        [1,1,1,1,1,1,1],    # 8
        [1,1,1,1,0,1,1]]    # 9

GPIO.setup(LedPIN, GPIO.OUT)        # LED 핀 모드 설정
GPIO.setup(SwitchPIN, GPIO.IN)      # SWITCH 핀 모드 설정
GPIO.setup(PiezoPIN, GPIO.OUT)      # Piezo buzzer 핀 모드 설정
pwm = GPIO.PWM(PiezoPIN, 262)

n1 = 0      # 4-digit FND 처음값 0000
n2 = 0
n3 = 0
n4 = 0

for segment in segments:            # segment 핀 모드 설정
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
for digit in digits:                # 4-digit FND 핀 모드 설정
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

def rc_time(CdsPIN):
    count = 0

    GPIO.setup(CdsPIN, GPIO.OUT)    # CDS 핀 모드 설정
    GPIO.output(CdsPIN, GPIO.LOW)
                                                      
    time.sleep(0.1)

    GPIO.setup(CdsPIN, GPIO.IN)     # CDS 핀 모드 설정

    while (GPIO.input(CdsPIN) == GPIO.LOW):     # 읽은 센서값이 HIGH가 될 때까지 count 수행 (즉, 센서 주변이 어두울 수록 카운트 값이 커짐)
        count += 1

    return count        # count값 반환

def display(digit, number):         # display(자릿수, 숫자)
    for i in range(len(digits)):    # 해당하는 자릿수 핀만 LOW 설정
        if i + 1 == digit:
            GPIO.output(digits[i], GPIO.LOW)
        else:
            GPIO.output(digits[i], GPIO.HIGH)

    for i in range(len(segments)):  # 숫자 출력
        GPIO.output(segments[i], data[number][i])
    time.sleep(0.001)

try:
    while True:
        if rc_time(CdsPIN) >= 70000:    # 조도센서 값이 일정 값보다 크면 LED는 키고 피에조부저는 끄기
            GPIO.output(LedPIN, GPIO.HIGH)
            pwm.stop()
            print("sleeping...")
        else:                           # 조도센서 값이 일정 값보다 작으면 LED는 끄고 피에조부저는 키기
            GPIO.output(LedPIN, GPIO.LOW)
            pwm.start(1)
            print("wake up!")
        while GPIO.input(SwitchPIN) == 1:   # 스위치가 눌러지면 디스플레이에 현재시각 표시
            now = datetime.now()            # 현재 시간 불러오기
            print("%02d:%02d"%((now.hour+8)%24, now.minute))
            pwm.stop()

            n1 = int(((now.hour+8)%24)/10)  # 각각 n1, n2, n3, n4에 숫자 넣기
            n2 = ((now.hour+8)%24)%10
            n3 = int(now.minute/10)
            n4 = now.minute%10
            
            display(1, n1)      # display(자릿수, 숫자)
            display(2, n2)
            display(3, n3)
            display(4, n4)
        if GPIO.input(SwitchPIN) == 0:      # 스위치가 눌러지지 않았다면 디스플레이 끄기
            GPIO.output(digits[3], GPIO.LOW)
            for i in range(7):
                GPIO.output(segments[i], 0)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()          # PWM 종료
    GPIO.cleanup()      # GPIO 핀 상태 초기화