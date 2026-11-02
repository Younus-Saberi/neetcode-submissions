class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        l1=sorted(s)
        l2=sorted(t)

        return l1==l2