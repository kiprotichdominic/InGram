import os
import requests

def get_posts():
    url = 'http://127.0.0.1:8000/api/v1/?format=json'
    r = requests.get(url)
    posts= r.json()
    return posts