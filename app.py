# #Find the second largest factor of a number (excluding the number itself)


# n = int(input("Enter Number: "))

# count = 2
# found = 0

# while count * count <= n:

#     if n % count == 0:

#         found += 1

#         factor = n // count

#         print("Small factor :", count)
#         print("Paired factor:", factor)

#         if found == 2:
#             print("Second largest factor =", factor)
#             break

#     count += 1

# else:

#     if found == 0:
#         print("Prime number")

#     elif found == 1:
#         print("Only one proper factor exists")



'''


n = int(input("Enter Number: "))
count=2
found=0

while count**2 <= n:
    if n%count == 0:
        found+=1

        pairedfactor=n//count # Small factor is count and the paired factor is the pairedfactor here

        if found == 2:
            print("Second Largest Factor: ",pairedfactor)

    count+=1

else:
    if found == 0:
        print("Prime Number")
    elif found == 1:
        print("Only one factor")



'''
''' 
n = int(input("Enter Number: "))

i=1
count=0
'''
'''
while i<n:
    if n%i == 0:
        count+=1
    i+=1

if count == 0:
    print("Not Prime")
else:
    print("Prime")

'''
'''

fruits=["Apple","Banana","Cherry","Kiwi","Guava" ]
fruits[2:]=["watermelon"]

print(fruits)

'''

'''


## List Methods

## append , insert , remove , pop , sort , reverse , clear



fruits=["Apple","Banana","Cherry","Kiwi","Guava" ]
fruits.append("Mango")
fruits.insert(1,"Pomegranate")
fruits.remove("Banana")
popped_fruits=fruits.pop()
# print(fruits.index("Apple"))
fruits.insert(1,"Pomegranate")
# print(fruits)
# print(fruits.count("Pomegranate"))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)





# print(popped_fruits)

'''

'''

## Slicing a List 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

'''



'''

### Iterating Over List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

# Iterating with index

for index, number in enumerate(numbers):
    print(f"{index}. {number}")

'''





# List Comphrension


'''
'''
# ##### List Comprehension

# Basics Syantax            [expression ,for item in iterable]

# with conditional logic    [expression , for item in iterable,  if condition]

# Nested List Comprehension [expression , for item1 in iterable1,  for item2 in iterable2 ]



'''




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

singleline_numbers=[number**2 for number in numbers]
print(singleline_numbers)





numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_squares=[num**2 for num in numbers if num%2==0 ]

print(even_squares)

# for num in range(numbers):
#     if num%2==0:
#         num**2



fruits=["Apple","Banana","Cherry","Kiwi","Guava" ]
nums = [1, 2, 3, 4, 5]

fruits_nums=[[i,j] for i in numbers for j in fruits ]
print(fruits_nums)
'''
        

# ## List Comprehension with function calls
# words = ["hello", "world", "python", "list", "comprehension"]
# lengths = [len(word) for word in words]
# print(lengths)  # Output: [5, 5, 6, 4, 13]


