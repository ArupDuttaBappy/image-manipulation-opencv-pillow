import cv2

img1 = cv2.imread('media/operation1.jpg')
img2 = cv2.imread('media/operation2.jpg')

and_img = cv2.bitwise_and(img1,img2)
or_img = cv2.bitwise_or(img1,img2)
xor_img = cv2.bitwise_xor(img1,img2)
not_img = cv2.bitwise_not(img1)

cv2.imshow('Bitwise AND', and_img)
cv2.imshow('Bitwise OR', or_img)
cv2.imshow('Bitwise XOR', xor_img)
cv2.imshow('Bitwise NOT', not_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
