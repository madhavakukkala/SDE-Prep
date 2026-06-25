# import json

# data = {
#     'name' : 'Madhav',
#     'class' : 'Graduate'
# }

# jsonstr = json.dumps(data)
# print(jsonstr)
# print(type(jsonstr))

# jsonjson = json.loads(jsonstr)
# print(jsonjson)
# print(type(jsonjson))


## CSV

# import csv

# with open('example.csv' ,mode='w', newline='') as file:
#     write = csv.writer(file)
#     write.writerow(['Name', 'age'])
#     write.writerow(['Madhav', 22])
#     write.writerow(['Balaji', 22])


# with open('example.csv' ,mode='r') as file:
#     writer = csv.reader(file)
#     for row in writer:
#         print(row)


# from datetime import datetime,timedelta

# bow=datetime.now()
# print(bow)
# print(bow+timedelta(days=100))

# import time
# print(time.time())
# time.sleep(1)
# print(time.time())
# time.sleep(1)
# print(time.time())


import re

pattern = r'\d+'
text = 'There are 123 apples'
match = re.search(pattern, text)
print(match.group())