# Working with images using python library

# execute inside directory => Complete-Python-3-Bootcamp-master/14-Working-with-Images/

from PIL import Image
mac = Image.open('example.jpg')
# Note this is a specialized file type from PIL (pillow)
type(mac)
mac.size
mac.filename
# (width, height)
# Output: 
# PIL.JpegImagePlugin.JpegImageFile
# (1993, 1257)
# 'example.jpg'
# 'JPEG (ISO 10918)'

# Cropping Images
# both x,y values below are coordinates
# (0,0) is top left corner
mac.crop((0, 0, 100, 100))
# pasting image
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))

# resizing image
new_h = int(h/3)
new_w = int(w/3)
# Note this is not permanent change
# for permanent change, do a reassignment
# e.g. mac = mac.resize((100,100))
mac.resize((new_h,new_w))
# can also stretch and squeeze
mac.resize((3000,500))
# can also rotate
# The original dimensions will be kept and "filled" in with black. You can optionally pass in the expand parameter to fill the new rotated image to the old dimensions.
mac.rotate(90)

pencils = Image.open("pencils.jpg")
# The image is cut off if you rotate by some odd degree
pencils.rotate(120)

# Transparency

# We can add an alpha value (RGBA stands for RED,Green,Blue, Alpha) where values can go from 0 to 255. If Alpha is 0 the image is completely transparent, if it is 255 then its completely opaque.
# You can create your own color here to check for possible values: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool
# We can adjust image alpha values with the putalpha() method:
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
red.putalpha(128); blue.putalpha(128)
blue.paste(red,box=(0,0),mask=red) # Get back an image that is more purple.

# Saving the image
blue.save("purple.png")
