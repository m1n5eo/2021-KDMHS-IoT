import cv2

img = cv2.imread('asdf.jpg')
img2 = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('asdf', img2)
cv2.imshow('asdf_GRAY', gray)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('asdf_GRAY.jpg', gray)

cv2.destroyAllWindows()