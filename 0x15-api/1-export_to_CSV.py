#!/usr/bin/python3
""" A script to export data in the CSV format in python"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userID)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userID)).json()
    with open("{}.csv".format(userID), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow([int(userID),
                                user.get('username'),
                                task.get('completed'),
                                task.get('title')])
