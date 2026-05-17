class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            chartup = [0] * 26
            for i in s:
                chartup[ord(i) - ord('a')] += 1
                
            if tuple(chartup) not in groups:
                groups[tuple(chartup)] = [s]
            else:
                groups[tuple(chartup)] = groups[tuple(chartup)] + [s]
        
        return list(groups.values())
            


            
        

        
        

    

