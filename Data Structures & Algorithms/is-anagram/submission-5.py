class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        for x in sl:
            if x in tl and len(s) == len(t):
                tl.remove(x)
            else:
                return False
        return True
        