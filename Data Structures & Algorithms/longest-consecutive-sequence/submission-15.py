class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        start = set()
        hm = {}
        set_len = len(start)
        for i in nums_set:
            if i-1 not in nums_set:
                start.add(i)
        for n in start:
            l = 1
            j = n+1
            while j in nums_set:
                j += 1
                l += 1
            max_len = max(l,max_len)

        return max_len
        