#!/usr/bin/python3
""" This module returns information about his/her TODO list progress,
using this REST API, for a given employee ID
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_ID = sys.argv[1]
    employee_url = ("{}/users/{}".format(url, employee_ID))
    todo_list_url = ("{}/todos?userId={}".format(url, employee_ID))
    r_employee = requests.get(employee_url)
    employee_json = r_employee.json()
    r_todo_list = requests.get(todo_list_url)
    todo_list_json = r_todo_list.json()
    employee_name = employee_json.get("name")
    n_task_done = 0
    for task in todo_list_json:
        if task.get("completed") is True:
            n_task_done += 1
    n_task_total = len(todo_list_json)
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, n_task_done, n_task_total))
    for task in todo_list_json:
        if task.get("completed") is True:
            task_title = task.get("title")
            print("\t {}".format(task_title, end=""))
