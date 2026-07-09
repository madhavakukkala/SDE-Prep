class Solution():

    # def palindrome(self,s):
    #     # print('*'.isalnum())
    #     pass

    def reversearr(self, i , arr):
        n = len(arr)
        if i > n//2:
            print(arr)
            return
            
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        self.reversearr(i+1,arr)



if __name__ == '__main__':
    sol = Solution()
    # s = 'A man, a plan, a canal: Panama'
    # lst = []
    # for i in s:
    #     if i.isalnum():
    #         lst.append(i)
    
    # a = "".join(lst).lower()
    # print(a)
    # print(a == a[::-1])
    # sol.palindrome(s)

    arr = list(map(int, input().split()))
    sol.reversearr(0,arr)
