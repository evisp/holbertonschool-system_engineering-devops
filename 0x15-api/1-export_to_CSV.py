#!/usr/bin/python3
"""Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = argv[1]
    user_request = requests.get(url + "users/{}".format(user)).json()
    all_requests = requests.get(url + "todos", params={"userId": user}).json()

    out_file = "{}.csv".format(user)
    with open(out_file, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        user_name = user_request['username']
        for request in all_requests:
            writer.writerow([user, user_name,
                             request['completed'],
                             request['title']])
