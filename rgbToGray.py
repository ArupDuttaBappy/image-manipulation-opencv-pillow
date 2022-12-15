from PIL import Image

img_rgb = Image.open('media/erock_rgb.jpg')
img_gray = img_rgb.convert('L')  # or '1'
img_gray.save('media/erock_gray2.jpg')
img_gray.show()
