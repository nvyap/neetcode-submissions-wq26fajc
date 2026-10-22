class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hm_prod = {}
        hm_prod_rev = {}
        p = 1
        p_rev = 1
        l = len(nums)
        result = []
        for i in range(len(nums)):
            p = p*nums[i]
            hm_prod[i] = p
            p_rev = p_rev*nums[l-i-1]
            hm_prod_rev[i] = p_rev
        for i in hm_prod:
            res_p = 1
            if i==0:
                res_p = hm_prod_rev[l-2]
            elif i==l-1:
                res_p = hm_prod[l-2]
            else: res_p = hm_prod[i-1]*hm_prod_rev[l-i-2]
            result.append(res_p)
        return result

