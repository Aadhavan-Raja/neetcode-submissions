class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            freqmap[num] = 1 + freqmap.get(num, 0)
        buckets = [[] for i in range(len(nums) + 1)]
        for num,freq in freqmap.items():
            buckets[freq].append(num)
        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
