n=int(input())
new=0
temp =n
while n>0:
    digit = n%10
    print(digit)
    new = new*10 + digit
    n//=10

if 