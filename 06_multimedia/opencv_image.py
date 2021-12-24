import cv2

img = cv2.imread('asdf.jpg')
img2 = cv2.resize(img, (1000, 800))

cv2.imshow('asdf', img2)

cv2.waitKey(0)

cv2.destroyAllWindows()