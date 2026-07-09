class Patterns():

    def __init__(self,n):
        self.n = n
        

    def pattern1(self):
        n = self.n

        for i in range(1,n+1):
            for j in range(1,n+1):
                print("*", end="")
            print()
        print("-------------------------------")

    def pattern2(self):
        n = self.n

        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*", end="")
            print()
        print("-------------------------------")

    def pattern3(self):
        n = self.n

        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end="")
            print()
        print("-------------------------------")

    def pattern4(self):
        n = self.n

        for i in range(n+1):
            for j in range(i):
                print(i, end="")
            print()
        print("-------------------------------")

    def pattern5(self):
        n = self.n

        for i in range(n):
            for j in range(n-i):
                print("*", end="")
            print()
        print("-------------------------------")

    def pattern6(self):
        n = self.n

        for i in range(n):
            for j in range(1,n-i+1):
                print(j, end="")
            print()
        print("-------------------------------")

    def pattern7(self):
        n = self.n

        for i in range(1,n+1):
            #spaces
            for j in range(1,n-i+1):
                print(" ", end="")

            #stars
            for j in range(1,2*i):
                print("*", end="")
            print()
        print("-------------------------------")


    def pattern8(self):
        n = self.n

        for i in range(1,n+1):
            #spaces
            for j in range(i-1):
                print(" ", end="")

            #stars
            for j in range(((2*n+1)-2*i)):
                print("*", end="")
            print()
        print("-------------------------------")


    def pattern9(self):
        n = self.n

        for i in range(1,n+1):
            #spaces
            for j in range(1,n-i+1):
                print(" ", end="")

            #stars
            for j in range(1,2*i):
                print("*", end="")
            print()


        for i in range(1,n+1):
            #spaces
            for j in range(i-1):
                print(" ", end="")

            #stars
            for j in range(((2*n+1)-2*i)):
                print("*", end="")
            print()
        print("-------------------------------")


    def pattern10(self):
        n = self.n

        # for i in range(1,2*n+1):
        #     if i<((2*n+1)/2):
        #         for j in range(1,i+1):
        #             print("*", end="")
        #     else:
        #         for j in range(2*n-i):
        #             print("*", end="")
        #     print()
                                                # -- or
        # for i in range(1, 2 * n):
        # if i <= n:
        #     stars = i
        # else:
        #     stars = 2 * n - i

        # for j in range(stars):
        #     print("*", end="")
        # print()
                                                # -- or
        for i in range(1,2*n+1):
            temp = min(i+1 , 2*n-i+1)
            for j in range(1,temp):
                print("*", end="")

            print()
        print("-------------------------------")
                

    def pattern11(self):
        n = self.n
        for i in range(1,n+1):
            if i%2 == 0:
                value = 0
            else:
                value = 1
            for j in range(1,i+1):
                print(value, end=" ")
                value = 1 - value
            print()
        print("-------------------------------")

    def pattern12(self):
        n = self.n
        for i in range(1,n+1):
            
            # numbers
            for j in range(1,i+1):
                print(j,end="")
            # spaces
            for j in range(1,n-i+1):
                print(" ",end="")
            # spaces
            for j in range(1,n-i+1):
                print(" ",end="")
            # numbers
            for j in range(i,0,-1):
                print(j,end="")
            print()
        print("-------------------------------")


    def pattern13(self):
        n = self.n
        number = 1
        for i in range(1,n+1):            
            for j in range(1,i+1):
                print(number,end=" ")
                number += 1
            print()
        print("-------------------------------")

    def pattern14(self):
        n = self.n
        for i in range(1,n+1):            
            for j in range(0,i):
                print(chr(65+j),end="")
            print()
        print("-------------------------------")

    def pattern15(self):
        n = self.n
        for i in range(n):            
            for j in range(n-i):
                print(chr(65+j),end="")
            print()
        print("-------------------------------")

    def pattern16(self):
        n = self.n
        for i in range(n):            
            for j in range(0,i+1):
                print(chr(65+i),end="")
            print()
        print("-------------------------------")


    def pattern17(self):
        n = 5
        for i in range(n):   
            #spaces         
            for j in range(1,n-i):
                print(" ",end="")

            #chars
            for j in range(2*i+1):
                if j < (2*i+1)/2:
                    chars = 65 + j
                else:
                    chars =  chars - 1
                print(chr(chars),end="")
            print()
        print("-------------------------------")


    def pattern18(self):
        n = self.n
        for i in range(1,n+1):   
            #chars
            for j in range(i,0,-1):
                chars = (65+n) - j
                print(chr(chars),end=" ")
            print()
        print("-------------------------------")

        # or it can  be written like this
        
        # n = self.n

        # for i in range(1, n + 1):
        #     start = 65 + (n - i)

        #     for j in range(i):
        #         print(chr(start + j), end=" ")

        #     print()


    def pattern19(self):
        n = self.n
        for i in range(1,2*n+1):  

            if i<(2*n+1)/2:
                # Upper Symmetry 
                #stars
                for j in range(n-i+1):
                    print("*",end="")

                #spaces
                spaces = 2*(i-1)+1
                for j in range(1,spaces):
                    print(" ",end="")
                
                #stars
                for j in range(n-i+1):
                    print("*",end="")

            else:

                # Lower Symmetry 
                #stars
                for j in range(i-n):
                    print("*",end="")

                #spaces
                spaces = 2 * (i-(2*(i-n)))
                for j in range(1,spaces+1):
                    print(" ",end="")
                
                #stars
                for j in range(i-n):
                    print("*",end="")
                    
            print()
        print("-------------------------------")


    def pattern20(self):
        n = self.n

        for i in range(2*n+1):


            if i<=n:
                 #stars
                for j in range(1,i+1):
                    print("*", end="")
                
                #spaces
                for j in range(1,2*(n-i)+1):
                    print(" ", end="")

                #stars
                for j in range(i,0,-1):
                    print("*", end="")
                print()
            else:
                #stars
                for j in range(1,(2*n-i+1)):
                    print("*", end="")
                
                #spaces
                for j in range(2*(i-n)):
                    print(" ", end="")

                #stars
                for j in range(1,(2*n-i+1)):
                    print("*", end="")
                print()


        print("-------------------------------")


    def pattern21(self):
        n = self.n
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==1 or i==n or j == 1 or j == n:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print("-------------------------------")


    def pattern22(self):
        n = self.n
        for i in range(2*n-1):
            for j in range(2*n-1):

                top = i
                left = j
                bottom = (2*n-2) - i
                right = (2*n-2) - j

                minDist = min(top,left,bottom,right)
                print(n - minDist , end=" ")
            print()
        print("-------------------------------")

            






pattern = Patterns(5)


pattern.pattern1()
pattern.pattern2()
pattern.pattern3()
pattern.pattern4()
pattern.pattern5()
pattern.pattern6()
pattern.pattern7()
pattern.pattern8()
pattern.pattern9()
pattern.pattern10()
pattern.pattern11()
pattern.pattern12()
pattern.pattern13()
pattern.pattern14()
pattern.pattern15()
pattern.pattern16()
pattern.pattern17()
pattern.pattern18()
pattern.pattern19()
pattern.pattern20()
pattern.pattern21()
pattern.pattern22()
