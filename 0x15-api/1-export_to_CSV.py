#!/usr/bin/python3
"""
Using a REST API, for a given employee ID, returns information about his/her
TODO list progess
"""
import csv
import requests
import sys


if __name__ == "__main__":
    """ Main method """
    api_url = "https://jsonplaceholder.typicode.com/"
    users_dict = requests.get('{}users/{}'.format(api_url, sys.argv[1])).json()
    user_name = users_dict.get('username')

    todo_dict = requests.get('{}todos?userId={}'.format(api_url,
                                                        sys.argv[1])).json()
    user_id = sys.argv[1]
    c_tasks = []
    for task in todo_dict:
            c_tasks.append([user_id, user_name, task.get('completed'),
                            task.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as f:
        employee_w = csv.writer(f, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in c_tasks:
            employee_w.writerow(task)
