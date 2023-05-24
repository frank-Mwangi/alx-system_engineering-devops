#!/usr/bin/python3
"""
Records task per employee in csv format
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(url).json()
    addr = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id)
    tasks = requests.get(addr).json()
    with open("{}.csv".format(id), 'w') as csvfile:
        listtasks = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            listtasks.writerow([id, user.get('username'),
                                task.get("completed"),
                                task.get("title")])
