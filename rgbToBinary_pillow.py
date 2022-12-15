from PIL import Image

col = Image.open("media/cat-tied-icon.png")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
bw.save("media/cat-tied-icon-binary.png")
bw.show()