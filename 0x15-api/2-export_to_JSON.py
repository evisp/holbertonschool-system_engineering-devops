#!/usr/bin/python3
"""Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = argv[1]
    user_request = requests.get(url + "users/{}".format(user)).json()
    all_requests = requests.get(url + "todos", params={"userId": user}).json()

    emp_data = []
    for request in all_requests:
        emp_data.append({
            "task" : request['title'],
            "completed" : request['completed'],
            "username" : user_request['username']
        })
    emp_data_json = {user: emp_data}

    with open("{}.json".format(user), "w") as file:
        json.dump(emp_data_json, file)
