n = int(input("Enter number: "))
num = str(n)
num  = num[::-1]
num = int(num)
if num == n:
    print("Yes its a palindrome")
else:
    print("No its not a palindrome")


