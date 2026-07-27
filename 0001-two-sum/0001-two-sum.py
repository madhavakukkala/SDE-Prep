class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mpp = {}
        arr = []
        for i in range(n):
            rem = target - nums[i]
            if rem in mpp:
                arr.append(mpp[rem])
                arr.append(i)
            mpp[nums[i]] = i
        return arr
        
        