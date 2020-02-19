import os
import requests

def get_posts():
    url = 'https://blogapi001.herokuapp.com/api/v1/'
    r = requests.get(url)
    posts= r.json()
    return posts                                                                                                                                                                                                                                                                                                                                                                                                                                            