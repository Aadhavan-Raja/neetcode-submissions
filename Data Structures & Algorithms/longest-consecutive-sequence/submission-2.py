class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        maxseq = 0;
        for i in nums:
            if i-1 not in hset:
                sequence = 1
                while i+1 in hset:
                    sequence += 1
                    i +=1
                if sequence > maxseq:
                    maxseq = sequence
        return maxseq
