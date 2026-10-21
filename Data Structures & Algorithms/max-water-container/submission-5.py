class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        r = len(heights)-1
        l = 0
        while l<r:
            a = (r-l)*min(heights[r],heights[l])
            max_a = max(a,max_a)
            if heights[r]>=heights[l]:
                l += 1
            else:
                r -= 1
        return max_a

        


        