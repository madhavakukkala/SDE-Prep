# Create a sample text file
with open('question1.txt', 'w') as file:
    file.write("Python is easy to learn.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.")

# Read only the first line
with open('question1.txt','r') as file:
    print(f"Line 1 : {file.readline()}")