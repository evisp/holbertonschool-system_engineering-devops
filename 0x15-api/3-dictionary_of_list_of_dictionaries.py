#!/usr/bin/python3
"""
Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == "__main__":
    jsonFile = 'todo_all_employees.json'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    user_req = requests.get(url_user).json()
    todo_req = requests.get(url_todo).json()
    json_format = {}
    for all_users in user_req:
        info_user_list = []
        for all_tasks in todo_req:
            if all_users['id'] == all_tasks['userId']:
                user_infor_dict = {
                    "username": all_users['username'],
                    "task": all_tasks['title'],
                    "completed": all_tasks['completed'],
                }
                info_user_list.append(user_infor_dict)
        json_format[all_users['id']] = info_user_list
    with open(jsonFile, "w") as file:
        json.dump(json_format, file)
