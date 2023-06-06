#!/usr/bin/python3
"""
Returns number of subscribers for given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    header = {"User-Agent": "WholeResponsible1801"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=header)

    if request.status_code == 200:
        return request.json()["data"]["subscribers"]
    else:
        return 0
