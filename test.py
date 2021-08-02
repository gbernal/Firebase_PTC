from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://rubikscode.net/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("a", class_='entry-featured-image-url')


image_info = []

for a in aas:
    image_tag = a.findChildren("img")
    image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))


def download_image(image):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum())

    file = open("/Users/gbernal/Documents/GitHub/Firebase_PTC/Data/Lego/{}.jpg".format(realname), 'wb')

    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response

for i in range(0, len(image_info)):
        download_image(image_info[i])
