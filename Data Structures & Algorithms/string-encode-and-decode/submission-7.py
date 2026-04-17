class Solution:
        # ['neet','code','is','good']
    def encode(self, strs: List[str]) -> str:
        encode=''
        for s in strs:
            encode+=str(len(s))+'#'+s
        return encode
        # [4#neet4#code2#is3#good]

    def decode(self, s: str) -> List[str]:
        decode=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=length+i
            decode.append(s[i:j])
            i=j

        return decode

