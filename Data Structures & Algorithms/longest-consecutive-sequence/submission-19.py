class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = []
        longest = 0
        nums_set = set(nums)
        for i in nums:
            if i-1 not in nums:
                start.append(i)
        
        for j in start:
            l = 0
            while j in nums_set:
                j += 1
                l += 1
                longest = max(longest,l)
        
        return longest


        