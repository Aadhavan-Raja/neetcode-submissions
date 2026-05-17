class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in strs:
            tup = [0] * 26
            for char in i:
                tup[ord(char) - ord('a')] += 1
            if tuple(tup) in hmap:
                hmap[tuple(tup)].append(i)
            else:
                hmap[tuple(tup)] = [i]
        return list(hmap.values())


            


            
        

        
        

    

