class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        hm = {}
        hm_rev = {}
        l = len(nums)
        for i in range(len(nums)):
            hm[i] = hm.get(i-1,1)*nums[i]

            hm_rev[i] =  hm_rev.get(i-1,1)*nums[l-i-1]

        

        for i in hm:
            result.append(hm.get(i-1,1)*hm_rev.get(l-i-2,1))

        return result
        