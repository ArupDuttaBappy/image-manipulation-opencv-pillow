import cv2

im = cv2.imread('home.jpg')
h, w, c = im.shape
print(int(w/2), int(h/2))
