import sys
sys.setrecursionlimit(100000)
class Recursive():




    def printNtimes(self,i,n):
        if i>n:
            return
        print(f"{i}. Madhav")

        self.printNtimes(i+1,n)

    def print1toN(self,i,n):
        if i>n:
            return
        self.print1toN(i+1,n)
        print(i)

    def printNto1(self,i,n):
        if i>n:
            return
        print(i)
        self.print1toN(i+1,n)

    def sumofN(self,n):
        if n==0:
            return 0    
        return n + self.sumofN(n-1)

    def factorial(self,n):
        if n==0:
            return 0
        else:
            if n==1:
                return 1
            return n * self.factorial(n-1)

    def reversearray(self,i):

        arr = [1,2,3,4,5,6]
        for item in range(1,len(arr)+1):
            new_arr.append(arr[len(arr)-item])
        
        print(new_arr)


        for i in range(len(arr)):
            temp[i] = arr[len(arr)-1-i]
        print(temp)

        left = 0
        right = len(arr) - 1

        while left<right:
            arr[left], arr[right]  = arr[right], arr[left]
            left +=1
            right -= 1
        print(arr)

    def revarr(self,i , arr, n):
        if i>n//2:
            print(arr)
            return
        
        arr[i] , arr[n-i-1] = arr[n-i-1], arr[i]

        self.revarr(i+1,arr,n)

    def palindrome(self,i,name):

        n = len(name)

        if i > n//2:
            return True


        if name[i] != name[n-i-1]:
            return False
        
        return self.palindrome(i+1,name)




        



        



obj = Recursive()
# obj.printNtimes(1,10)
# obj.print1toN(1,10)
# print(obj.sumofN(100))
# print(obj.factorial(7))


arr = [1,2,3,4,5,6]
# obj.revarr(0,arr,len(arr))
print(obj.palindrome(0,'duad'))
# obj.reversearray(0)
