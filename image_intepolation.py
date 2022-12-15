import cv2
import numpy as np

img = cv2.imread('media/apple.jpg')
# cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
nn_img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)
bl_img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
bc_img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Nearest-Neighbour Interpolation", nn_img)
cv2.imshow("Bi-Linear Interpolation", bl_img)
cv2.imshow("Bi-Cubic Interpolation", bc_img)

cv2.waitKey(0)
cv2.destroyAllWindows()