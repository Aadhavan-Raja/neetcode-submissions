class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for value,key in enumerate(nums):
            hmap[key] = value
        for i in range(len(nums)):
            looking = target-nums[i]
            if looking in hmap and i != hmap[looking]:
                return [i,hmap[looking]]