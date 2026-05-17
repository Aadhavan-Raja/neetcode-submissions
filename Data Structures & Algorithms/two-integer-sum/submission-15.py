class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for key, value in enumerate(nums):
            map[value] = key

        for i in nums:
            if target - i in nums and nums.index(i) != map[target-i]:
                return [nums.index(i), map[target-i]]
