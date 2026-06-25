# n=int(input("Enter number: "))
'''
integer = 1

for i in range(1,n+1):
    for j in range(1,i+1):
        print(integer, end=" ")
        integer +=1 
        
    print()

'''

'''
for i in range(n+1):
        for char in range(65,65+i):
            print(chr(char), end=" ")
        print()

'''
'''

for i in range(n):
        for char in range(n-i):
            print(chr(65 + char), end="")   
        print()
'''

'''
breakpoint = int(0)
for i in range(n):
    #spaces
    for j in range(1,n-i+1):
        print(" ", end="")

    #Letters
    for j in range(2*i+1) :
        print(chr(65 + j), end="")      
        if breakpoint == (2*i+1)/2:
            print(chr(65 - j), end="")      

    #Spaces
    for j in range(1,n-i+1):
        print(" ", end="")
    print()
'''

# a=0
# for i in range(n):
#     for j in range(65 + (n-1)-i,65+n):
#         print(chr(j), end=" ")
#     print()

# a=0
# for i in range(n):
#     for j in range(65 + (n-1)-i,65+n):
#         print(chr(j), end=" ")
#     print()





'''
You are given an array arr, replace every element in that array
 with the greatest element among the elements to its right, and 
 replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [2,4,5,3,1,2]

Output: [5,5,3,2,2,-1]

'''


# arr = [2,4,5,3,1,2]
# def replace_elements(arr):
#     n = len(arr)
#     ans = [0] * n
#     right_max = -1

#     for i in range(n - 1, -1, -1):
#         ans[i] = right_max
#         right_max = max(arr[i], right_max)

#     return ans

# print(replace_elements(arr))



def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Added sprinkles")
        func()
    return wrapper

@add_sprinkles
def get_icecream(flavor):
    print(f"Here is your {flavor} Icecream")


get_icecream("vanilla")