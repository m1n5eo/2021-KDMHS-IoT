# 카메라로 얼굴 인식하기

import cv2

# model, config 파일 설정
model = './dnn/res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = './dnn/face_deploy.prototxt'

# 카메라 가져오기
cap = cv2.VideoCapture(0)

# Load a pre-trained network
net = cv2.dnn.readNet(model, config)

while True:
    _, frame = cap.read()
    if frame is None:
        break

    # blob 이미지 생성
    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 117, 123))

    # blob 이미지를 네트워크 입력으로 설정
    net.setInput(blob)

    # 네트워크 실행 (순방향)
    detect = net.forward()
    detect = detect[0, 0, :, :]

    (h, w) = frame.shape[:2]

    # 얼굴 인식을 위한 반복
    for i in range(0, detect.shape[0]):
        # 얼굴 인식 확률 추출
        confidence = detect[i, 2]
        if confidence < 0.5:
            break

        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * h)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = 'Face: %4.3f' % confidence
        cv2.putText(frame, label, (x1, y1-1),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()