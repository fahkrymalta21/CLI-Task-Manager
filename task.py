import json

data = {
    "id": 1,
    "description": "Belajar Python Dasar",
    "status": "todo",
    "createdAt": "2023-10-27 10:00"
}

with open("task.json", "w") as task:
    json.dump(data, task, indent=4)

# json_string = json.dumps(data, indent=4)
# print(json_string)