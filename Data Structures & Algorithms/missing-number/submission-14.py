class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        r = 0
        hs = {}
        for i,n in enumerate(nums):
            hs[n] = i
        while r<=l:
            if r not in hs:
                return r
            r += 1
        
        
            
        