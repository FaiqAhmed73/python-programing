import requests
from io import BytesIO
from PIL import Image
r = requests.get("https://www.14thstreetpizza.com/website/images/pizzasizes/full-v1.jpg")

print("status code", r.status_code)

image = Image.open(BytesIO(r.content))



print(image.size, image.format, image.mode)
path ="./image.jpg" 

try:
    image.save(path, image.format)
except IOError:
    print("cannnot save image")
