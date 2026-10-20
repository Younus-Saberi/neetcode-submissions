class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        if len(nums)<=0:
            return False
        for i in nums:
            if i not in hset:
                hset.add(i)
            else:
                return True
        
        if len(hset)!=0:
            return False