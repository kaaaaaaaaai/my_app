# load image from url
img_bytes = urlopen('https://image.shutterstock.com/image-illustration/vector-illustration-mathematical-formula-on-600w-1427881685.jpg').read()
import base64
img_b64 = base64.b64encode(img_bytes)