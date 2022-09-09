#!/usr/bin/python3
"""
Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
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

    csvfile = "{}.csv".format(user_id)
    with open(csvfile, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        username = user_req['username']
        for all_tasks in todo_req:
            writer.writerow([user_id, username,
                            all_tasks['completed'],
                            all_tasks['title']])
