class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p1 = 1
        p2 = 1
        l = len(nums)-1
        pref = []
        suff = []
        hm = {}
        res = []
        for i in range(len(nums)):
            p1 = p1*nums[i]
            p2 = p2*nums[l-i]
            pref.append(p1)
            suff.append(p2)
        print(pref)
        print(suff)

        for j in range(len(nums)):
            if j != 0 and j != l:
                res.append(suff[l-j-1]*pref[j-1])
            elif j==0:
                res.append(suff[l-1])
            elif j==l:
                res.append(pref[l-1])
        return res
                
        




        

        