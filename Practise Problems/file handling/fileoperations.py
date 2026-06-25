## Read a whole file

# with open('example.txt', 'r')as file:
#     content = file.read()
#     print(content)

## rad a file line by line

# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line.strip())


## write a gile (overwrite)
'''
with open('example.txt', 'w') as file:
    file.write('Hello World , of the 2026!\n')
    file.write('This is a new line!')
'''
    

## write a file without overwriting
'''
with open('example.txt', 'a') as file:
    file.write('Append operation taking place')
'''

## Writing a list of lines
'''
lst  = ['First line \n','Second line \n','Third line \n']
with open('example.txt', 'a') as file:
    file.writelines(lst)
'''

## Binary files

'''
data = b'\x00\x01\x02\x03\x04'

with open('example.bin', 'wb') as file:
    file.write(data)

print("Binary file written successfully")

with open('example.bin', 'rb') as file: ## read binary
    content = file.read()
    print(content)
'''



## Practical examples

## I want to read the content from a source text file and write it to a destination text file 
'''
with open('example.txt','r') as file:
    content = file.read()
with open('destination.txt','w') as file:
    dest = file.write(content)
'''


file = open('example.txt', 'w')
data = file.write("how are you")
file.close()

with open('new.txt', 'w') as file:
    data = file.write("I am a software engineer with 5 years of experience \n")
    data = file.write("I am soft \n")
    data = file.write("I love teaching \n")
    data = file.write("I like to travel alot \n")

with open('new.txt', 'r') as file:
    # line1 = file.readline()
    # line2 = file.readline()
    # line3 = file.readline()
    # line4 = file.readline()
    # print(f"Line 1 : {line1}")
    # print(f"Line 2 : {line2}")
    # print(f"Line 3 : {line3}")
    # print(f"Line 4 : {line4}")
    # print(data)
    readlines = file.readlines()
    print(readlines)







  



# ## read a text file , count the number of lines , words , chararcters
# lines = []
# chars = []
# words = []
# with open('example.txt', 'r') as file:
#     for line in file:
#         lines.append(line)
# with open('example.txt', 'r') as file:
#     chars = list(file.read())


    
# print(f" Number of lines: {len(lines)}") 
# print(f" Number of characters: {len(chars)}") 


 

