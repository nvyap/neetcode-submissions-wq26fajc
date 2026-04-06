class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hm = {}
        for i in nums:
            l = 0
            if i-1 not in nums:
                l = 1
                hm[i] = []
                j = i+1
                while j in nums:
                    l += 1
                    j += 1
            max_len = max(max_len,l)
        return max_len

                     
        
                
            

        