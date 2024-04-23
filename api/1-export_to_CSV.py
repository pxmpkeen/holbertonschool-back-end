#!/usr/bin/python3
"""
Saving to CSV
"""

if __name__ == '__main__':
    import requests
    import sys
    import os

    user_name_url = "https://jsonplaceholder.typicode.com/users/{:d}"
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={:d}"
    final_str = "Employee {:s} is done with tasks({:d}/{:d}):"
    formatted_str = "\"{:d}\",\"{}\",\"{}\",\"{}\"\n"

    user_id = int(sys.argv[1])
    user_name = requests.get(user_name_url.format(user_id)).json().get("name")
    todos = requests.get(todos_url.format(user_id)).json()

    titles = [
            todo.get("title") for todo in todos if todo.get(
                "completed"
                ) is True
            ]
    total_num = len(todos)
    done_num = len(titles)

    string = final_str.format(user_name, done_num, total_num)

    csv_str = ""
    for todo in todos:
        csv_str += formatted_str.format(
                user_id, user_name, todo.get("completed"), todo.get("title")
                )

    with open("{:d}.csv".format(user_id), "w") as fp:
        fp.write(csv_str)
