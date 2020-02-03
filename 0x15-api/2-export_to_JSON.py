#!/usr/bin/python3
""" This module export data in the JSON format.
"""

import requests
import sys
import json
from collections import OrderedDict


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_ID = sys.argv[1]
    employee_url = ("{}/users/{}".format(url, employee_ID))
    todo_list_url = ("{}/todos?userId={}".format(url, employee_ID))
    r_employee = requests.get(employee_url)
    employee_json = r_employee.json()
    r_todo_list = requests.get(todo_list_url)
    todo_list_json = r_todo_list.json()
    employee_usrname = employee_json.get("username")
    json_name = "{}.json".format(employee_ID)
    with open(json_name, 'w') as json_file:
        for task in todo_list_json:
            task_completed = task.get("completed")
            task_title = task.get("title")
            todo_dict = {employee_ID: [{"task": task_title,
                                        "username": employee_usrname,
                                        "completed": task_completed}]}
            json_file.write(json.dumps(OrderedDict(sorted(todo_dict.items()))))
