import os
##m print how many lines are present in notes.txt

with open('notes.txt', 'w') as file:
    file.write("Python is easy to learn.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.")


## now let us find how many lines

with open('notes.txt', 'r') as file:
    data = file.readlines()

print(f"There are {len(data)} lines in the file")



