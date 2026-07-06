class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hm = {}
        nums_set = set(nums)
        for i in nums_set:
            if i-1 not in nums_set:
                m = 0
                while i in nums_set:
                    m += 1
                    i += 1
                if m>max_len:
                    max_len = m
        return max_len
                     


        