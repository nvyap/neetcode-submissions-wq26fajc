class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hm = {}
        for i in nums:
            if i-1 not in nums:
                m = 0
                while i in nums:
                    m += 1
                    i += 1
                if m>max_len:
                    max_len = m
        return max_len
                     


        