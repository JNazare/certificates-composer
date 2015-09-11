import base64

png_encode = "data:image/png;base64,"
img_folder = "img/"
def encode_image(filename):
	with open(filename, "rb") as image_file:
		png_str = png_encode + base64.b64encode(image_file.read())
	image_file.close()
	return png_str
