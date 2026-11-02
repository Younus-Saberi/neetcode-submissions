class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        count = [0]*26

        i=0
        n=len(s)

        while i<n:
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
            i+=1

        for val in count:
            if val!=0:
                return False
        return True