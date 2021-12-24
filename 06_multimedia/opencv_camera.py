import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

# 사진 찍기
# ret, frame = cap.read()
# cv2.imshow('fram', frame)
# cv2.waitKey(0)
# cv2.imwrite('output.jpg', frame)

# 동영상 촬영
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 13: # 1000->1초, 100->0.1초
        break

cap.release()
cv2.destroyAllWindows()