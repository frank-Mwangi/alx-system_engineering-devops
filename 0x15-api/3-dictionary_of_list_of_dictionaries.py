#!/usr/bin/python 3
"""
Records all tasks from all employees in
JSON format
"""

import json
import requests


if __name__ == "__main__":
    filename = "todo_all_employees.json"
    res = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    res_id = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    with open(filename, "w") as file:
        d = {j.get("id"): [{'task': i.get('title'),
                            'completed': i.get('completed'),
                            'username': j.get('username')} for i in res
                           if j.get("id") == i.get('userId')]
             for j in res_id}
        json.dump(d, file)
