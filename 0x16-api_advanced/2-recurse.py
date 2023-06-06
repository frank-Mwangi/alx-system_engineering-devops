#!/usr/bin/python3
"""
Lists all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    header = {
        "User-Agent": "WholeResponsible1801"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        articles = response.json()["data"]
        after = articles["after"]
        count += articles["dist"]
        for child in articles["children"]:
            hot_list.append(child["data"]["title"])
    else:
        return None

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
