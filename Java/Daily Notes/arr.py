## From given numbers , we sbhould find the greatest number 


n = int(input("How many numbers : ")) 
nums  = []

for i in range(n):
    nums.append(int(input())) 

largest = nums[0]

for j in range(n):
    if nums[j] > largest:
        largest = nums[j]
    

print(f"The largest number if {nums} is {largest}")



