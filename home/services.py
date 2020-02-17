import os
import requests

def get_posts():
    url = 'https://blogapi001.herokuapp.com/api/v1/?format=json'
    r = requests.get(url)
    posts= r.json()
    return posts