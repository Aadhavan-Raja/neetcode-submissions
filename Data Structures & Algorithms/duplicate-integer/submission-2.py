class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = nums
        y = set(nums)
        if len(x) == len(y):
            return False
        return True