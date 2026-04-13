class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hm = {}
        start = []
        nums_set = set(nums)

        for i in nums:
            if i-1 not in nums:
                start.append(i)

        
        
        for j in start:
            l = 1
            while j in nums_set:
                max_len = max(max_len,l)
                l += 1
                j += 1
                
        return max_len

            

        