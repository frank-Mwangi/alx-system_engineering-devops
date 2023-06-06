#!/usr/bin/python3
"""
Lists top 10 hot posts for given subreddit
"""

import requests


def top_ten(subreddit):
    header = {"User-Agent": "WholeResponsible1801"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    parameters = {
        "limit": 10
    }

    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)
    if response.status_code == 200:
        hot_list = response.json().get("data")
        for hot in hot_list.get("children"):
            print(hot.get("data").get("title"))
    else:
        print("None")
        return
