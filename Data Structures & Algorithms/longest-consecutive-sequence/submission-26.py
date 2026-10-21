class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        begin = []

        for i in nums_set:
            if i-1 not in nums_set:
                begin.append(i)
        length = 0
        for n in begin:
            num = n+1
            l = 1
            while num in nums_set:
                l += 1
                num += 1
            length = max(l,length)
        
        return length
