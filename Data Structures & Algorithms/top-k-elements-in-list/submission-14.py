class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Kmap = {}

        for num in nums:
            if num in Kmap:
                Kmap[num] += 1
            else:
                Kmap[num] = 1

        knums = [[] for _ in range(len(nums) + 1)]
        
        for num,v in Kmap.items():
            knums[v].append(num)

        answer = []

        for i in range(len(nums),0, -1):
            for i in knums[i]:
                answer.append(i)
                if len(answer) == k:
                    return answer
        
