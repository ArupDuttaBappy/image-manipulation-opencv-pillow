import cv2
import matplotlib.pyplot as plt

image_br1 = cv2.imread('media/br1.jpg')
image_br2 = cv2.imread('media/br2.jpg')

cv2.resize(image_br1, (300,300))
cv2.resize(image_br2, (300,300))

cv2.imshow("Resized Image 1", image_br1)
cv2.imshow("Resized Image 2", image_br2)

cv2.waitKey(0)
cv2.destroyAllWindows()