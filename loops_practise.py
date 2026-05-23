#Print numbers from 1 to N

# N=int(input("Number: "))

# for i in range(N+1):
#     print(i)


#Print numbers from N to 1

# N=int(input("Number: "))

# for i in range(N,0,-1):
#     print(i)


#. Print all even numbers from 1 to N

# N=int(input("Number: "))

# for i in range(0,N+1,2):
#     print(i)


#. Print all even numbers from 1 to N

# N=int(input("Number: "))

# for i in range(0,N+1,2):
#     print(i)


# Find sum of first N natural numbers

# N=int(input("Number: "))
# sum=0
# i=0

# while i<=N:
#     sum += i
#     i+=1

# print(sum)


# Find factorial of a number

# N=int(input("Number: "))
# result=1

# for i in range (1,N+1):
#     result *= i

# print(result)


#Count number of digits in a number

# N=int(input("Number: "))
# count=0

# while N>0:
#     N = N//10
#     count+=1

# print(count)


#Reverse a number

# N=int(input("Number: "))
# reverse=0

# while N>0:

#     digit = N%10
#     # print(digit)
#     reverse=reverse*10+digit

#     N=N//10


# print(reverse)


    
#Check if palindrome


# N=int(input("Number: "))
# M=N

# reverse=0

# while N>0:
#     digit = N%10

#     reverse = reverse *10 + digit

#     N//=10

# if M == reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")



#Find sum of digits 

# N=int(input("Number: "))


# sum=0

# while N>0:
#     digit = N%10

#     sum = sum + digit

#     N//=10

# print(sum)


#Finding the largest digit of a number 

# N=int(input("Number: "))
# largest=0

# while N>0:
#     digit = N%10

#     if digit > largest:
#         largest = digit

#     N//=10

# print(largest)

# Find smallest digit in a number


# N=int(input("Number: "))
# smallest=9

# while N>0:
#     digit = N%10

#     if digit < smallest:
#         smallest = digit

#     N//=10

# print(smallest)


#Check if a number is prime


# N=int(input("Number: "))
# i=2

# while i<N:
#     if N%i==0:
#         print("Not Prime")
#         break
#     i+=1

# else:
#     print("Prime")




#Print all prime numbers from 1 to N

# n=int(input("Number: "))
# print(f"Printing Prime numbers from 1 to {n} are ....")

# for x in range(2,n+1):
#     for y in range(2,x):
#         if x % y == 0:
#             break
#     else:
#         print(x, end=", ")



# # Print all prime numbers from 1 to N

# N = int(input("Enter Number: "))

# num = 2

# while num <= N:

#     divisor = 2

#     while divisor < num:

#         if num % divisor == 0:
#             break

#         divisor += 1

#     else:
#         print(num)

#     num += 1


# 5. Find all factors of a number

# n=int(input("Enter number for factors: "))
# # factor=0
# i=1
# print(f"Factors of {n} are.....")

# while i<=n:
#     if n%i==0:
#         print(i,end=" ")
#     i+=1

#Findiing the largest factor of a number

# n=int(input("Enter number for factors: "))
# first_factor=2
# found=0
# while first_factor**2<=n:
#     if n%first_factor==0:
#         paired_factor=n//first_factor
#         found+=1

#         if found==2:    # if found is 1 >> first ;argest factor || if found is 2 >> second largest factor
#             print(paired_factor)

#     first_factor+=1
# else:
#     if found==0:
#         print("Prime Number")
#     elif found==1:
#         print("Only one Factor")


#Check if a number is a perfect square
# for i in range(1,5):

#     n=int(input("Enter Number: "))

#     i=0

#     while (i+1)**2<=n:
#         i+=1

#     print(i)



#19. Check if a number is an Armstrong number
# Example:
# 153 = 1³ + 5³ + 3³

# n=int(input("Enter number: "))
# while n>0:
#     n//=10

    
# for h in range(1,6):

#     n=int(input("Enter Number: "))
#     m=n
#     k=n
#     final_armstrong=0
#     count=0
#     while n>0:
#         n//=10
#         count+=1
#     while m>0:
#         digit = m%10
#         check_armstrong_digits= digit**count
#         final_armstrong=final_armstrong+check_armstrong_digits    

#         m//=10
        

#     if final_armstrong==k:
#         print("Armstrong")
#     else:
#         print("Not armstrong")




#Fibonacci series


# n=int(input("Enter Number: "))

# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")


# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     if c <= n:
#         print(c,end=" ")



# STAR Patterns
# n=5
# # Print Number Pyramid

# rows = 4

# for i in range(1, rows + 1):

#     for j in range(1, i+1):

#         print(j, end="")

#     print()





## Final 2 questions test
'''

Write a program to check whether a number is a Strong Number or not.

Example
Input: 145
Output: Strong Number

Because:

1! + 4! + 5! = 145

'''

# Given that if a number is given , i should follow the steps
# 1. extract digits
# 2.find factorials 
# 3.sum up and cehck with the fieest number 

# then its a strong nnumber 

# this might be the psuedocode 
'''

n=int(input("Enter number to check: "))
m=n

print("Checking whether strong number or not...")

## first step tp extract digits 

i=0
factorial =1
temp=factorial
sum=0

while n>0:
    digit = n%10

    for i in range(1,digit+1):
        temp*=i
    sum=sum+temp

    temp=factorial

    n//=10

# print(sum)

if sum==m:
    print(f"Yes , {m} is a strong number")
else:
    print(f"No , {m} is not a strong number")


'''


# Write a program to print all PRIME numbers from:

# 1 to N

# in REVERSE order.

# 📊 Example

# Input:

# 20

# Output:

# 19 17 13 11 7 5 3 2


'''
Given that i should do this :

1. print all prime numbers form 1 to N

2. I should rpint them in reverse order 


'''

'''
n=int(input("Enter N value: "))

for x in range(n,1,-1):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print( x ,end=" ")

'''

'''

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)
'''



## Program for findiing perfect squares from 1 to N

# first iterate from 1 to that N 
# then find out of any of the number has perfect square


# N=int(input("Enter N: "))

# lst=[]
# for i in range(1,N+1):
#     for j in range(1,i):
#         if i==j**2:  
#             lst.append(i)
#             # print(i)

# print(lst)


# N=int(input("Enter N: "))

# for i in range(1,N+1):
#     if i**2<N:
#         print(i**2) 
    