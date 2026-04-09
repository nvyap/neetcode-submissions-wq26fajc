class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l = len(heights)
        for ind,val in enumerate(heights):
            i = ind+1
            while i<l:
                h = min(val,heights[i])
                vol = h*(i-ind)
                max_vol = max(max_vol,vol)
                i += 1

        return max_vol
        