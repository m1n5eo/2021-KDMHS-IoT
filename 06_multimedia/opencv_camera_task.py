import cv2

# 카메라 장치를 열기
cap = cv2.VideoCapture(0) #카메라 디바이스 번호

if not cap.isOpened():
    print('Camera Open Failed')
    exit()

# 카메라 사진 찍기
# ret, frame = cap.read() # ret : 정상 / 비정상 & frame 이미지 데이타
# cv2.imshow('frame', frame)
# cv2.waitKey(0)
# cv2.imwrite('output.jpg', frame)

#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break

edge = cv2.Canny(frame, 50, 100)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.imshow('frame', frame)
cv2.imshow('gray', gray)
cv2.imshow('edge', edge)

# 1000-> 1초 10 -> 0.01초
if cv2.waitKey(10) == 13:
    break

cap.release()
cv2.destroyAllWindows()