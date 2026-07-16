class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        n = len(nums)
        # step 1
        j = -1
        for i in range(0,n):
            if nums[i] == 0:
                j = i
                break
        
        # step 2
        for m in range(j+1,n):
            if nums[m] != 0 and nums[j] == 0:
                nums[j],nums[m] = nums[m],nums[j]
                j+=1

            