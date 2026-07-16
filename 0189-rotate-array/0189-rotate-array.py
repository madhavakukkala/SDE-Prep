class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        k = n-k
        temp = nums[:k]

        for i in range(k,n):
            nums[i-k] = nums[i]
        j = 0
        for m in range(n-k,n):
            nums[m] = temp[j]
            j+=1
