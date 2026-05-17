class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        smap = {}
        tmap = {}

        for i in s:
            if i in smap.keys():
                smap[i] = smap[i] + 1
            else:
                smap[i] = 0
        
        for i in t:
            if i in tmap.keys():
                tmap[i] = tmap[i] + 1
            else:
                tmap[i] = 0
        
        return tmap == smap
        

       

