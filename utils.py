#!/usr/bin/python1
import json

# json parser
def load_json(file):
    # open json file
    with open(file, encoding='utf-8') as json_data:
        data = json.loads(json_data.read())

    insert_department_list = []
    insert_employee_list = []

    # iterate over json data 
    for a in data:
        if a["Type"] == 3:
            insert_employee_list.append(
                tuple((
                    a["id"],
                    a["Name"],
                    a["ParentId"],
                )))
        elif a["Type"] == 1 or a["Type"] == 2:
            insert_department_list.append(
                tuple((
                    a["id"],
                    a["Name"],
                    a["ParentId"],
                )))

    #return strings
    department_str = ', '.join(str(e) for e in insert_department_list).replace(
        "None", "NULL")
    employee_str = ', '.join(str(e) for e in insert_employee_list).replace(
        "None", "NULL")

    return department_str, employee_str