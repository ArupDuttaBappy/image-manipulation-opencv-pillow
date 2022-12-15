from PIL import Image

image_br1 = Image.open('media/br1.jpg')
image_br2 = Image.open('media/br2.jpg')

new_image_br1 = image_br1.resize((400, 400))
new_image_br2 = image_br2.resize((400, 400))

new_image_br1.save('br1_400.jpg')
new_image_br2.save('br2_400.jpg')