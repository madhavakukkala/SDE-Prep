## from a given number , we have to total nnumber of even digits and odd digits


# input : 435217
# even : 2
# odd : 4


# n = int(input("Enter number: "))
# even = 0
# odd = 0

# while (n>0):
#     digit = n%10
#     if digit%2 == 0:
#         even = even+1
#     else:
#         odd = odd + 1
    
#     n = n//10

# print(f"Even : {even}")
# print(f"Odd : {odd}")




# n=50

# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         print(i)

# m = int(input("Number 1: "))
# n = int(input("Number 2: "))

# m = max(m,n)
# n= min(m,n)

# print(m//n)

nums = [0,1,0,3,12]
n = len(nums)

new_nums=[]

for i in range(0,n):
    if nums[i] != 0:
        new_nums.append(nums[i])

while len(new_nums) < len(nums):
    new_nums.append(0)


print(new_nums)





