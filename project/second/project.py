import RPi.GPIO as GPIO
import cv2
import time

SwitchPIN = [0, 19, 13, 6, 5, 11, 9, 10, 22, 27]   # Switch GPIO 핀번호를 리스트로 선언
CGH_SwitchPIN = 17  # 4-digit FND에 적힌 번호를 초기화할 때 사용할 Switch GPIO 핀번호를 변수로 선언
SeeDisplaySwitchPIN = 26    # 4-digit FND에 적힌 번호를 확인할 때 사용할 Switch GPIO 핀번호를 변수로 선언
PiezoPIN = 3        # Piezo buzzer GPIO 핀번호를 변수로 선언
ServoPIN = 2        # Servo Motor GPIO 핀번호를 변수로 선언
segments = [21, 20, 16, 12, 7, 8, 25]   # segment GPIO 핀번호를 리스트로 선언
digits = [24, 23, 18, 15]               # 4-digit FND GPIO 핀번호를 리스트로 선언
data = [[1,1,1,1,1,1,0],    # 0     4-digit FND에 표시될 숫자의 데이터
        [0,1,1,0,0,0,0],    # 1
        [1,1,0,1,1,0,1],    # 2
        [1,1,1,1,0,0,1],    # 3
        [0,1,1,0,0,1,1],    # 4
        [1,0,1,1,0,1,1],    # 5
        [1,0,1,1,1,1,1],    # 6
        [1,1,1,0,0,0,0],    # 7
        [1,1,1,1,1,1,1],    # 8
        [1,1,1,1,0,1,1]]    # 9
n = [0, 0, 0, 0]        # 4-digit FND 처음값 0000
passwd = [1, 2, 3, 4]   # Password
cnt = 0

cap = cv2.VideoCapture(0)   # 카메라 장치 열기

GPIO.setmode(GPIO.BCM)      # 초기 GPIO 설정

for switch in SwitchPIN:    # Switch 핀 모드 설정
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CGH_SwitchPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Switch 핀 모드 설정
GPIO.setup(SeeDisplaySwitchPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # Switch 핀 모드 설정

GPIO.setup(PiezoPIN, GPIO.OUT)      # Piezo buzzer 핀 모드 설정
pwmPiezo = GPIO.PWM(PiezoPIN, 262)
pwmPiezo.stop()

GPIO.setup(ServoPIN, GPIO.OUT)      # Servo Motor 핀 모드 설정
pwmServo = GPIO.PWM(ServoPIN, 50)
pwmServo.start(11)

for segment in segments:            # segment 핀 모드 설정
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
for digit in digits:                # 4-digit FND 핀 모드 설정
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

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
        for i in range(1, 10): # 키패드의 비밀번호가 맞으면 문을 열고 틀리면 피에조부저를 울리는 부분
            if GPIO.input(SwitchPIN[i]) == 0 and n[cnt] == 0: # 스위치가 눌러졌고 n[cnt]에 0이 들어있다면
                n[cnt] = i
                cnt += 1
                time.sleep(0.5)
                if cnt == 4: # cnt가 4라면, 즉, 비밀번호 4자리가 모두 입력이 되었다면
                    cntCorrect = 0
                    for i in range(4):
                        if n[i] == passwd[i]:
                            cntCorrect += 1
                    if cntCorrect == 4: # 비밀번호가 맞았다면
                        print("Correct")
                        pwmServo.ChangeDutyCycle(7) # 서브모터를 통해 문을 열어주기
                        time.sleep(2)
                        pwmServo.ChangeDutyCycle(11)
                    else: # 비밀번호가 틀렸다면
                        print("Wrong Password")
                        pwmPiezo.start(1) # 피에조부저를 1초동안 울림
                        time.sleep(1)
                        pwmPiezo.stop()
                    for i in range(4):
                        n[i] = 0
                    cnt = 0
        
        if GPIO.input(CGH_SwitchPIN) == 0:      # CGH_SwitchPIN 스위치가 눌러지면 리스트 n과 cnt 0으로 초기화 해주기
            n[0] = 0
            n[1] = 0
            n[2] = 0
            n[3] = 0
            cnt = 0
        
        while GPIO.input(SeeDisplaySwitchPIN) == 0:    # SeeDisplaySwitchPIN 스위치가 눌러지면 디스플레이에 누른 숫자 표시
            display(1, n[0]) # display 함수로 들어감(4-digit FND의 첫번째 자리에 n[0]을 출력해줌)
            display(2, n[1]) # display 함수로 들어감(4-digit FND의 두번째 자리에 n[1]을 출력해줌)
            display(3, n[2]) # display 함수로 들어감(4-digit FND의 세번째 자리에 n[2]을 출력해줌)
            display(4, n[3]) # display 함수로 들어감(4-digit FND의 네번째 자리에 n[3]을 출력해줌)

        if GPIO.input(SeeDisplaySwitchPIN) == 1:      # SeeDisplaySwitchPIN 스위치가 눌러지지 않았다면 디스플레이 끄기
            GPIO.output(digits[3], GPIO.LOW)
            for i in range(7):
                GPIO.output(segments[i], 0)
        
        ret, frame = cap.read()     # 카메라 사진 찍기
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) == 27:   # 10ms 기다린 후 다음 프레임 처리 / ESC키가 입력되면 while문을 빠져나감
            break

except KeyboardInterrupt:
    pass

finally:
    cap.release()       # 사용자 자원 해제
    cv2.destroyAllWindows()     # 열려있는 모든 창 닫기
    pwmServo.stop()     # pwmServo 끄기
    pwmPiezo.stop()     # pwmPiezo 끄기
    GPIO.cleanup()      # GPIO 핀 상태 초기화