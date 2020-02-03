#!/usr/bin/python3
""" This module export data in the JSON format.
"""

import json
from collections import OrderedDict
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_url = ("{}/users".format(url))
    r_employee = requests.get(employee_url)
    employee_json = r_employee.json()
    json_name = "todo_all_employees.json"
    with open(json_name, 'w') as json_file:
        dict_of_dicts = OrderedDict()
        for employee in employee_json:
            employee_ID = employee.get("id")
            employee_usrname = employee.get("username")
            todo_list_url = ("{}/todos?userId={}".format(url, employee_ID))
            r_todo_list = requests.get(todo_list_url)
            todo_list_json = r_todo_list.json()
            todo_list = []
            for task in todo_list_json:
                task_completed = task.get("completed")
                task_title = task.get("title")
                todo_dict = {"username": employee_usrname,
                             "task": task_title,
                             "completed": task_completed}
                todo_list.append(OrderedDict(todo_dict))
            dict_of_dicts[employee_ID] = todo_list
        json_file.write(json.dumps(dict_of_dicts))
