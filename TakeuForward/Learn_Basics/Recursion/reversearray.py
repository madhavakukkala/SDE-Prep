class Solution():

    def reversearray(self,i, arr,n):

        # left = 0
        # right = len(arr)-1
        i = 0
        n = len(arr)

        while i < n//2:
            arr[i] , arr[n-1-i] =  arr[n-1-i] , arr[i]

            i+=1

        return arr
    
    def revarr(self,arr):

        tabe = list(reversed(arr))
        print(tabe)

if __name__ == '__main__':
    sol = Solution()
    arr = list(map(int,input().split()))
    # print(sol.reversearray(0,arr,5))
    (sol.revarr(arr))
