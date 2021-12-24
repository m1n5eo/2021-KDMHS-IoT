# 이미지 분류(Image Classification)

import cv2
import numpy as np

# model, config, classFile 설정
model = './dnn/bvlc_googlenet.caffemodel'
config = './dnn/deploy.prototxt'
classFile = './dnn/classification_classes_ILSVRC2012.txt'

classNames = None
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load a pre-trained neural network
net = cv2.dnn.readNet(model, config)

# 이미지 파일 읽기
img = cv2.imread('cat.jpg')

# blob 이미지 생성
blob = cv2.dnn.blobFromImage(
    img, scalefactor=1, size=(224, 224), mean=(104, 117, 123))

# blob 이미지를 네트워크 입력으로 설정
net.setInput(blob)

# 네트워크 실행 (순방향)
detections = net.forward()

# 가장 높은 값을 가진 클래스 얻기
out = detections.flatten()
classId = np.argmax(out)
confidence = out[classId]

# 분류 결과 출력
text = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)
cv2.putText(img, text, (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
