class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for value,key in enumerate(nums):
            hmap[key] = value
        for i in range(len(nums)):
            look = target - nums[i]
            if look in hmap and i != hmap[look]:
                return [i, hmap[look]]



