import cv2

img = cv2.imread('home.jpg')
img_v = cv2.flip(img, 0)
cv2.imshow("Vertical Flip", img_v)
cv2.waitKey(0)
cv2.destroyAllWindows()
