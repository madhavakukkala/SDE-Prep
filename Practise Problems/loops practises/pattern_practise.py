
def pattern1(n):
    # outer loop
    for i in range(1,n+1):
        #Inner Loop
        for j in range(1,n+1):
            print("* " , end="")
        print()


def pattern2(n):
    # outer loop
    for i in range(1,n+1):
        #Inner Loop
        for j in range(1,i+1):
            print("*", end="")
        
        print()


def pattern3(n):
    # outer loop
    for i in range(1,n+1):
        #Inner Loop
        for j in range(1,i+1):
            print(j, end="")
        
        print()




def pattern4(n):
    # outer loop
    for i in range(1,n+1):
        #Inner Loop
        for j in range(1,i+1):
            print(i, end="")
        
        print()




def pattern5(n):
    # outer loop
    for i in range(n,0,-1):
        #Inner Loop
        for j in range(1,i+1):
            print("*", end="")
        
        print()


def pattern6(n):
    # outer loop
    for i in range(1,n+1):
        #Inner Loop
        for j in range(0,n-i+1):
            print("*", end="")
        
        print()






number = int(input("Enter n: "))

# pattern1(number)
# print()
# # pattern2(number)
# print()
# pattern3(number)
# pattern4(number)
# pattern5(number)
pattern6(number)



