import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpend():
    print('Camera open failed')
    exit()

# fourcc(four character code)
# DIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

# 동영상 촬영
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 13: # 1000->1초, 100->0.1초
        break

cap.release()
out.release()
cv2.destroyAllWindows()