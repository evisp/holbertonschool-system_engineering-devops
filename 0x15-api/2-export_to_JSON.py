#!/usr/bin/python3
"""
Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(user_id)
    user_req = requests.get(url_user).json()
    userId_parameter = '?userId={}'.format(user_id)
    url_todo = 'https://jsonplaceholder.typicode.com/todos{}'\
        .format(userId_parameter)
    todo_req = requests.get(url_todo).json()
    todo_total = len(todo_req)

    info_list = []
    for all_tasks in todo_req:
        tasks_infor_dict = {
                "task": all_tasks['title'],
                "completed": all_tasks['completed'],
                "username": user_req['username'],
        }
        info_list.append(tasks_infor_dict)
    json_format = {user_id: info_list}

    jsonFile = "{}.json".format(user_id)
    with open(jsonFile, "w") as file:
        json.dump(json_format, file)
