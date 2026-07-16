class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums_new = [x for x in nums if x!=0]
        zeronums = [x for x in nums if x==0]
        nums_new.extend(zeronums)
        nums[:] = nums_new[:]
        
