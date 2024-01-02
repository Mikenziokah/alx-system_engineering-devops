#!/usr/bin/python3
"""script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    """ Main method """
    api_url = "https://jsonplaceholder.typicode.com/"
    users_dict = requests.get('{}users/{}'.format(api_url, sys.argv[1])).json()
    print("Employee {} is done with tasks".format(users_dict.get('name')),
          end="")

    todo_dict = requests.get('{}todos?userId={}'.format(api_url,
                                                        sys.argv[1])).json()
    c_tasks = []
    for task in todo_dict:
        if task.get("completed") is True:
            c_tasks.append(task)

    print("({}/{}):".format(len(c_tasks), len(todo_dict)))
    for task in c_tasks:
        print("\t {}".format(task.get('title')))
