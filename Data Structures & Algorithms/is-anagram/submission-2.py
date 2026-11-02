class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        firstDict = {}
        secondDict = {}

        
        def countFreq(v,dict):
            dict[v] = 1 + dict.get(v,0)

        i=0
        n=len(s)

        while i<n:
            countFreq(s[i],firstDict)
            countFreq(t[i],secondDict)
            i+=1

        return firstDict==secondDict
