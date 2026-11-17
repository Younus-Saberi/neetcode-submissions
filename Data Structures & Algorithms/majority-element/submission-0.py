class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap={}
        for n in nums:
            hmap[n]=1+hmap.get(n,0)
        return max(hmap, key=hmap.get)
