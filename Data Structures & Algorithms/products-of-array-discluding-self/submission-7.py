class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        back = []
        p1 = 1
        p2 = 1
        res = []
        l = len(nums)-1
        for i in range(len(nums)):
            p1 = p1*nums[i]
            forward.append(p1)
            p2 = p2*nums[l-i]
            back.append(p2)
        
        for i in range(len(nums)):
            if i == 0:
                prod = back[l-i-1]
            elif i == l:
                prod = forward[l-1]
            else:
                prod = forward[i-1]*back[l-i-1]
            res.append(prod)

        return res
            
        

        