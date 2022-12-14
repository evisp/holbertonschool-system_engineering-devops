#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = argv[1]
    user_request = requests.get(url + "users/{}".format(user)).json()
    all_requests = requests.get(url + "todos", params={"userId": user}).json()

    completed_tasks = []
    for request in all_requests:
        if request['completed']:
            completed_tasks.append(request)

    print("Employee {} is done with tasks({}/{}):".format(user_request.get('name'), len(completed_tasks), len(all_requests)))

    for task in completed_tasks:
        print("\t {}".format(task['title']))
