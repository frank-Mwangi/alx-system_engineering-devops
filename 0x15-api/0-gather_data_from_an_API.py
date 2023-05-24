#!/usr/bin/python3
"""
Returns info about an employee's todo
list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    toDo = requests.get(url + "todos?userId={}".format(id)).json()
    name = user.get("name")
    done = 0
    totalTasks = 0
    for task in toDo:
        totalTasks += 1
        if task.get('completed') is True:
            done += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, totalTasks))
    for task in toDo:
        if task.get('completed') is True:
            print("\t {}".format(task.get("title")))
