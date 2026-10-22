class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = 0
        while l<r:
            a = min(heights[r],heights[l])*(r-l)
            max_area = max(max_area,a)
            if heights[l]>heights[r]:
                r -= 1
                continue
            if heights[r]>heights[l]:
                l += 1
                continue
            else:
                l += 1
                #r -= 1
        return max_area
            
        