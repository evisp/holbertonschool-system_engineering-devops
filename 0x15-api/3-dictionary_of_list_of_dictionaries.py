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
from sys import argv

if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    user_request = requests.get(url_users).json()
    all_requests = requests.get(url_todos).json()

    emp_data_json = {}
    for users in user_request:
        emp_data = []
        for request in all_requests:
            if users['id'] == request['userId']:
                emp_data.append({
                    "username" : users['username'],
                    "task" : request['title'],
                    "completed": request['completed']
                })
        emp_data_json[users['id']] = emp_data

    with open("todo_all_employees.json", "w") as file:
        json.dump(emp_data_json, file)
