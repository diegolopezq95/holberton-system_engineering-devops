#!/usr/bin/python3
""" This module export data in the CSV format.
"""

import csv
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
    employee_usrname = employee_json.get("username")
    csv_name = "{}.csv".format(employee_ID)
    with open(csv_name, 'w') as csv_file:
        for task in todo_list_json:
            task_completed = task.get("completed")
            task_title = task.get("title")
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow([employee_ID, employee_usrname,
                                 task_completed, task_title])
