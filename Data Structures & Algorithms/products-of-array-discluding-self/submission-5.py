class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_reg = []
        prod_rev = []
        prod_fwd = 1
        prod_back = 1
        res = []
        l = len(nums)
        for i in range(len(nums)):
            prod_fwd = prod_fwd*nums[i]
            b = l-i-1
            prod_back = prod_back*nums[b]
            prod_reg.append(prod_fwd)
            prod_rev.append(prod_back)
        
        for j in range(len(nums)):
            f_idx = j - 1
            b_idx = (l - 1) - (j + 1)
            
            prefix = prod_reg[f_idx] if f_idx >= 0 else 1
            suffix = prod_rev[b_idx] if b_idx >= 0 else 1
            
            res.append(prefix * suffix)
        return res