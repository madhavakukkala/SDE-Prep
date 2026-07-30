class Solution:
    def sortColors(self, nums) -> None:
        count_00 = count_01 = count_02 = 0
        for num in nums:
            if num == 0:
                count_00 += 1
            elif num == 1:
                count_01 += 1
            elif num == 2:
                count_02 += 1
        
        for i in range(count_00):
            nums[i] = 0
        for i in range(count_00,count_00+count_01):
            nums[i] = 1
        for i in range(count_00+count_01,len(nums)):
            nums[i] = 2

        return nums