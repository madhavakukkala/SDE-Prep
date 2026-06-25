# ## Temperature Conversion

# '''

# def convert_temperature(temp,unit):
#     """ This function converts temperature between Celcius and Farenheit"""

#     if unit=="C":
#         return temp *9/5 +32 ## Converting Celcius to Fahrenheit
#     elif unit== "F":
#         return (temp-32)*5/9 ## Fahrenheit to Celcius
#     else:
#         return None
    

# print(convert_temperature(25,"C"))
# print(convert_temperature(77,"F"))

# '''

# ## Password Strength Checker


# '''

# numbers=[1,2,3,4,5,6,7]

# lst= list(map( lambda x:x**2, numbers))
# print(lst)

# ## Map multiple Iterables

# numbers1=[1,2,3]
# numbers2=[4,5,6]

# added_numbers=list(map(lambda x,y:x+y , numbers1,numbers2))

# print(added_numbers)

# '''

# # list_new=[1,2,3,5,4,57,4,4,34,76,54]

# # list_naya=list(filter(lambda x:x%2==0, list_new))

# # print(set(list_naya))


# # ## filter() to check the age is greater than 25 in dictionary



# # people=[
# #     {'name': 'Kukkapilla', 'age' : 22},
# #     {'name': 'Budankay', 'age' : 21},
# #     {'name': 'Bunny', 'age' : 3},
# #     {'name': 'Chittipapa', 'age' : 0.5},
# # ]

# # def age_greater_than_20(person):
# #     return person['age']>19

# # print(list(filter(age_greater_than_20, people)))



# #map()


# numbers  = []

# # list(map(int(input("Enter Number: ")),numbers))


# n=int(input("count: "))
# nums = list(map(int, input().split))[:n]

# print(nums)

# def display_invoice(username , amount , due_date):

#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due : {due_date}")


# display_invoice("Madhav Reddy", 234, "23-4-54")

# def happynumber(N):
#     temp = N
    
#     while temp>0:
#         while temp > 0:

#             sum = 0
#             while temp>0:
#                 digit = temp%10
#                 sum += (digit**2)
#                 temp//=10

#             if sum == 1:
#                 return True
#             elif sum == 4:
#                 return False
            
#             temp = sum


# N = int(input("Number: "))

# happyis = False

# while happyis == False:

#     if happynumber(N):
#         print(N)
#         happyis = True

#     else:
#         N = N+1

    
    



# digit = 0
# # n = int(input("Number: "))
# temp = n
# while temp>0:
#     sum = 0
#     while temp>0:
#         digit = temp%10
#         sum += pow(digit,2)
#         temp//=10
    
#     if sum == 1:
#         print(True) 
#         break
#     elif sum == 4:
#         print(False) 
#         break

#     temp = sum


# doubles = [x*2 for x in range(1,11) ]
# triples = [y*3 for y in range(1,11) ]
# squares = [z**2 for z in range(1,11) ]

# print(doubles)
# print(triples)
# print(squares)


import math as budankay

print(budankay.pi)