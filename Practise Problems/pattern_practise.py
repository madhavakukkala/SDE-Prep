

def square_pattern(n):

    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
    
def right_angled_triangle_pattern(n):

    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

def right_angled_triangle_number_pattern(n):

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def right_angled_triangle_number_repeat_pattern(n):

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end=" ")
        print()
    
def right_angled_triangle_inverted_pattern(n):

    for i in range(0,n+1):
        for j in range(0,n-i):
            print("*" ,end=" ")
        print()
    
    
def right_angled_triangle_inverted__number_pattern(n):

    for i in range(0,n+1):
        for j in range(1,n-i+1):
            print(j ,end=" ")
        print()
    
    
def pyramid_pattern(n):

    for i in range(0,n):
        # space

        for j in range(0,n-i-1):
            print(" ", end=" ")
        # star
        
        for j in range(0,2*i+1):
            print("*" , end=" ")
        # space

        for j in range(0,n-i-1):
            print(" ", end=" ")
        
        print()
    
    
def pyramid_inverted_pattern(n):

    for i in range(0,n):
        # space

        for j in range(0,i):
            print(" ", end=" ")
        # star
        
        for j in range(0,2*n - (2*i + 1)):
            print("*" , end=" ")
        # space



        for j in range(0,i):
            print(" ", end=" ")
        
        print()


    
def right_angled_twice_mirrored_number_pattern(n):
    space =2*(n-1)

    for i in range(0,n):
        # space

        for j in range(1,i+1):
            print(j, end=" ")
        # star
        
        for j in range(1,space+1):
            print(" " , end=" ")
        # space



        for j in range(i,0,-1):
            print(j, end=" ")
        
        print()
        space -= 2
    
def pattern13(n):

    num=1
    for i in range(n+1):
        for i in range(1,i+1):
            print(num, end=" ")
            num += 1
        
        print()


def pattern14(n):
    for i in range(n+1):
        for char in range(65,65+i):
            print(chr(char), end="")
        print()
    





for num in range(1,4):
    n=int(input(f"Test Case {num}: "))

    # square_pattern(n)
    # right_angled_triangle_pattern(n)
    # right_angled_triangle_number_pattern(n)
    # right_angled_triangle_number_repeat_pattern(n)
    # right_angled_triangle_inverted_pattern(n)
    # right_angled_triangle_inverted__number_pattern(n)
    # pyramid_pattern(n)
    # pyramid_inverted_pattern(n)
    # right_angled_twice_mirrored_number_pattern(n)
    # pattern12(n)
    pattern14(n)


    