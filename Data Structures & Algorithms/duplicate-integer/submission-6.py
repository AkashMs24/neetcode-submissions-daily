class Solution:
    def hasDuplicate(self,nums):
        if len(nums) != len(set(nums)):
            return True
        else:
            return False