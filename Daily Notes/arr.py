for i in range(,100):
    for j in range(2,i+1):
        if i%j!=0:
            break
    else:
        print(i, end=" ")
        


# n=int(input("Number: "))
# print(f"Printing Prime numbers from 1 to {n} are ....")

# for x in range(2,n+1):
#     for y in range(2,x):
#         if x % y == 0:
#             break
#     else:
#         print(x, end=", ")
