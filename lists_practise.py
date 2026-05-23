'''
my_set={1,2,3,4,5,6,77,7,6,4}
print(my_set)

my_empty_set={}

my_empty_set=set([1,2,3,4,4,4,5])

print(my_empty_set)

'''
##Basic Set Operations
'''
my_set={1,2,3,4,5,6,77,7,6,4}

my_set.discard(60)
print(my_set)



set_1=my_set.pop()
print(set_1)
print(my_set)

'''

## Set membership Test
'''
set_1={1,2,3,4,5}
set_2={4,5,6,7,8,9}

union_set=set_1.union(set_2)
intersection_set=set_1.intersection(set_2)
print(union_set)
print(intersection_set)

set_1.intersection_update(set_2)
print(set_1)


'''

## Diffference 

'''

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

print(set1.difference(set2))
print(set1)

##Symmetric Difference
set1.symmetric_difference(set2)

'''


## Set Methods
'''
lst=[1,2,3,4,5,6,6,7,8,9,10]

print(set(lst))
print(set)

'''


## COunting unique words in text

'''
text = "In this Tutorial we are going to discuss about sets"

words=text.split()

print(words)
words_set=set(words)

print(words_set)
print(len(words_set))

'''



#### Conclusion
# Sets are a powerful and flexible data type in Python that provide a way to store collections of unique elements. They support various operations such as union, intersection, difference, and symmetric difference, which are useful for mathematical computations. Understanding how to use sets and their associated methods can help you write more efficient and clean Python code, especially when dealing with unique collections and membership tests.


## Dictionaries

'''
jyothi={"name":"jyothi","age":16,"grade":9.7}

print(jyothi)

print(jyothi['grade'])
print(jyothi.get('grade'))

jyothi['grade']=21

print(jyothi['grade'])

jyothi['address']="Chirala"


print(jyothi)

del jyothi['address']

print(jyothi)

'''
## Dictionary Methods
'''
jyothi={"name":"jyothi","age":16,"grade":9.7}

keys=jyothi.keys()
print(keys)

values=jyothi.values()
print(values)

items=jyothi.items()
print(items)

student=jyothi.copy() ## Shallow copy

jyothi['name']="Roshan"

print(student)
print(jyothi)

'''


## Iterating over Dictionaries
'''
jyothi={"name":"jyothi","age":16,"grade":9.7}

for key,value in jyothi.items():
    print(f"{key}:{value}")

'''

## NEsted Dictionaries
'''
students = {
    "jyothi":{"Age":16, "Class":10, "Grade":98} ,
    "roshan":{"Age":14, "Class":8, "Grade":100}

}


for student,name in students.items():
    print(f"{student}: {name}")
    for key,value in name.items():
        print(f"{key}:{value}")


# m=str(input("Enter name: "))
# for x,y in students[m].items():
#     print(f"{x} - {y}")


'''


## USe a dictionary to count he frequency of elements in list

'''
numbers=[0.1,0.1,0.1,0.2,0.2,0.3,0.4,0.3,0.5,0.4,0.3,0.5,0.7,0.3,0.1,0.0,0.8]

frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1

print(frequency)


frequency["hello"]="world"

print(frequency)



'''


## Print first element and last element.
'''
lst=[11,12,3,4,32,5,63,0,70,10]
largest=lst[0]
count=0
second_largest=0

for num in lst:
    
    if num>largest:
        second_largest=largest
        largest=num


    elif num>second_largest:
        second_largest=num


        # count+=1
        
print(second_largest)
print(largest)
    
'''
'''
FOR every number:

    if bigger than largest:
        move largest into second_largest
        update largest

    elif bigger than second_largest:
        update second_largest

'''



##Check whether element exists in list.
'''
lst = [1, 2, 3, 4, 5]
target=int(input("Element to check:"))

if target in lst:
    print("Element exists")
else:
    print("Element does not exist")

# for num in lst:
#     if num==target:
#         print("Element exist")
#         break
# else:
#     print("Element does not exist")


'''

'''

Question: Count Frequency of an Element in a List

Write a program that takes a list of integers and a target element as input, then prints how many times the target element appears in the list.

Input Format
First line: space-separated integers representing the list
Second line: integer x (the element to count)
Output Format
Print the frequency of x in the list
Example

Input

1 2 3 2 4 2 5
2

Output

3
Constraints
Length of list ≥ 1
Elements can be positive, negative, or zero
Expected Difficulty

Basic list traversal and counting.

Follow-up

Solve it:

Using a loop
Using the built-in count() method


'''

nums = list(map(int, input().split()))
x = int(input())


