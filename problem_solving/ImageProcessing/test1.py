from PIL import Image

image_obj = Image.open("devOps.png")

#To see image in explorer
#image_obj.show()

#To print image in matrix form
print(image_obj)

print(image_obj.size)

new_image = image_obj.resize((400, 400))

#new_image = new_image.rotate(75)
new_image.rotate(18).save('image_rot_18.png')
#new_image.show()

#Flipping Images
#You can also flip images to get their mirror version. This is done with the transpose() function. It takes one of the following options: PIL.Image.FLIP_LEFT_RIGHT, PIL.Image.FLIP_TOP_BOTTOM, PIL.Image.ROTATE_90, PIL.Image.ROTATE_180, PIL.Image.ROTATE_270 or PIL.Image.TRANSPOSE.
new_image = image_obj

image_flip = new_image.transpose(Image.FLIP_LEFT_RIGHT)

image_flip.show()
