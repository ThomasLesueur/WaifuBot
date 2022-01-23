import requests
import os

def get_random_image_url():
    res = requests.get('https://api.waifu.pics/sfw/waifu')
    return res.json()["url"]

def download_image(url):
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return filename

def remove_image(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")