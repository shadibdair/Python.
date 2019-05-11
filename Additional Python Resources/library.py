import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://data.arab48.com/data/news/2015/06/12/1159877/1434107179991995.jpg")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")