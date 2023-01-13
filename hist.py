import cv2
from matplotlib import pyplot as plt

img = cv2.imread('home.jpg')
# hist = cv2.calcHist([img],[0],None,[256],[0,256])

colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.show()
