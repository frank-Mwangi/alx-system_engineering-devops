#/usr/bin/python3
"""
Returns info about an employee's todo
list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        id = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, id))
        username = req.json().get("name")
        if username is not None:
            jsonreq = requests.get(
                "{}todos?userId={}".format(
                    url, id)).json()
            totaltasks = len(jsonreq)
            donetasks = []
            for i in jsonreq:
                if i.get("completed") is True:
                    donetasks.append(i)
            count = len(donetasks)
            print("Employee {} is done with tasks({}/{}):"
                  .format(username, count, totaltasks))
            for task in donetasks:
                print("\t {}".format(task.get("title")))
