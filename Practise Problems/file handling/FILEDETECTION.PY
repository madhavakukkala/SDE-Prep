# import os


# file_path = "C:\\Users\\aspir\\Desktop"

# if os.path.exists(file_path):
#     print(f"the location {file_path} exists")

# else:
#     print("The location doesnt exist")

# if os.path.isfile(file_path):
#     print("That is a file")
# elif os.path.isdir(file_path):
#     print("That is a directory")
import json
import csv
employees = [
    ["Rahul", 25, "Developer"],
    ["Priya", 28, "Designer"],
    ["Arjun", 30, "Manager"],
    ["Sneha", 26, "Tester"],
    ["Kiran", 32, "Analyst"]
]


file_path = 'output.csv'

with open(file_path, 'w', newline="") as file:
    raayi = csv.writer(file)
    for row in employees:
        raayi.writerow(row)
    print("File created")


