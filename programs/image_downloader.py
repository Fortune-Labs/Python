import random
import urllib.request

def download_web_image(url):
    name = random.randrange(100)
    full_name = str(name) + "jpg"
    urllib.request.urlretrieve(url,full_name)
download_web_image()
