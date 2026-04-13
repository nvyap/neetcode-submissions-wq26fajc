class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []
        l = len(nums)-1
        res = [0]*len(nums)
        
        p1 = 1
        p2 = 1

        for i in range(len(nums)):
            p1 = p1*nums[i]
            p2 = p2*nums[l-i]
            pref.append(p1)
            suff.append(p2)
        print(pref)
        print(suff)    
        for j in range(len(nums)):
            if j == 0:
                res[j] =suff[l-j-1]
            
            elif j == l:
                res[j] = pref[j-1]

            else:
                res[j] = suff[l-j-1]*pref[j-1]

        return res

            


