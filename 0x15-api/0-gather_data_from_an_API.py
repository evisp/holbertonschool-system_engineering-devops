#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

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

    tasks_done = []
    for check in todo_req:
        if check['completed']:
            tasks_done.append(check)
    total_tasks_done = len(tasks_done)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_req['name'], total_tasks_done, todo_total))

    for titles in tasks_done:
        print("\t {}".format(titles['title']))
