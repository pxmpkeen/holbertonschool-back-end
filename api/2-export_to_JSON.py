#!/usr/bin/python3
"""
Saving to CSV
"""

if __name__ == '__main__':
    import requests
    import sys
    import os
    import json

    user_name_url = "https://jsonplaceholder.typicode.com/users/{:d}"
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={:d}"

    user_id = int(sys.argv[1])
    user_name = requests.get(user_name_url.format(user_id)).json().get(
            "username"
            )
    todos = requests.get(todos_url.format(user_id)).json()

    tasks = [{
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": user_name
        } for todo in todos]
    final_dict = {str(user_id): tasks}
    with open("{:d}.json".format(user_id), "w") as fp:
        fp.write(json.dumps(final_dict))
