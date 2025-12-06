import json

# data = {
#     "id": 1,
#     "description": "Belajar Python Dasar",
#     "status": "todo",
#     "createdAt": "2023-10-27 10:00"
# }

# with open("task.json", "w") as task:
#     json.dump(data, task, indent=4)

# json_string = json.dumps(data, indent=4)
# print(json_string)

perintah = ""
while (perintah != "Stop"):
    perintah = input("Perintah: ")
    if (perintah == "Add"):
        print("Tambah To Do List")
    elif (perintah == "Remove"):
        print("Hapus To Do List")
    elif (perintah == "Edit"):
        print("Edit To Do List")