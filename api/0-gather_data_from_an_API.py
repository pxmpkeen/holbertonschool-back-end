#!/usr/bin/python3
"""
Starting with API
"""

if __name__ == '__main__':
    import requests
    import sys

    user_id = int(sys.argv[1])
    user_name = requests.get(
            "https://jsonplaceholder.typicode.com/users/{:d}".format(user_id)
            ).json().get("name")
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={:d}".format(
                user_id
                )
            ).json()

    titles = [
            todo.get("title") for todo in todos if todo.get(
                "completed"
                ) is True
            ]
    total_num = len(todos)
    done_num = len(titles)

    string = "Employee {:s} is done with tasks({:d}/{:d}):".format(
            user_name, done_num, total_num
            )
    print(string)
    for title in titles:
        print("\t {:s}".format(title))
