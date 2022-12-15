import cv2

img = cv2.imread('media/erock_rgb.jpg')

height, width, channels = img.shape  # color image
img_bytes = (height * width * channels) / 8
compressed_bytes = img.size
compression_ratio = img_bytes/compressed_bytes

print("Image Bytes:", img_bytes)
print("Compressed Bytes:", compressed_bytes)
print("Compression Ratio:",compression_ratio)