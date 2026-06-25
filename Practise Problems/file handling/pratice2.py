
# with open('practise2.txt','w') as file:
#     file.write("Python is easy\n")
#     file.write("I love  coding\n")
#     file.write("I am lazy\n")
#     file.write("I am still trying to learn\n")


# Total number of lines
with open('practise2.txt','r') as file:
    line = file.readlines()
print(f"Total number of lines: {len(line)}")


# Total number of words
with open('practise2.txt','r') as file:
    words = file.read().split()
print(f"Total number of words: {len(words)}")

#Total number of characters
with open('practise2.txt','r') as file:
    chars = list(file.read())
lst = []
for char in range(len(chars)):
    if not chars[char] == " " and not chars[char] == "\n":
        lst.append(chars[char])
print(f"Total number of Letters: {len(lst)}")

# Longest word in the file
with open('practise2.txt','r') as file:
    all_list = list(file.read().split())

print(f"Longest word in the file: {")


