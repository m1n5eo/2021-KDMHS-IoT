# 이미지 파일로부터 얼굴 인식하기

import cv2

# model, config 파일 설정
model = './dnn/res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = './dnn/face_deploy.prototxt'

# 이미지 파일 읽기
img = cv2.imread('imageFile.jpg')

# Load a pre-trained network
net = cv2.dnn.readNet(model, config)

# blob 이미지 생성
blob = cv2.dnn.blobFromImage(img, 1, (300, 300), (104, 117, 123))

# blob 이미지를 네트워크 입력으로 설정
net.setInput(blob)

# 네트워크 실행 (순방향)
detect = net.forward()
detect = detect[0, 0, :, :]

(h, w) = img.shape[:2]

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

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    label = 'Face: %4.3f' % confidence
    cv2.putText(img, label, (x1, y1-1),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

cv2.destroyAllWindows()