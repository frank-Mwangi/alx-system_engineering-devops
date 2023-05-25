#!/usr/bin/python3
"""
Record all tasks owned by an employee
Export this data in JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(id)).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(argv[1])).json()

    with open("{}.json".format(id), "w") as userId:
        json.dump({id: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': users.get('username')
        } for task in tasks]}, userId)
