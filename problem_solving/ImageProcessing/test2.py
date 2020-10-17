from PIL import Image, ImageDraw

image_obj = Image.open("sunshine.jpg")
logo_img = Image.open("timepass.jpg")

#print(image_obj, logo_img)
image_obj1 = image_obj.copy()
position = ((image_obj1.width - logo_img.width), (image_obj1.height - logo_img.height))


image_obj1.paste(logo_img, position)
image_obj1.show()