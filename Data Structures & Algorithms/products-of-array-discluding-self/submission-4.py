class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0]*len(nums)
        suff = [0]*len(nums)
        res = [0]*len(nums)
        l = len(nums)-1
        p1, p2 = 1,1

        for i in range(len(nums)):
            p1 = nums[i]*p1
            p2 = nums[l-i]*p2
            pref[i] = p1
            suff[l-i] = p2

        for j in range(len(nums)):
            if j == 0:
                res[j] = suff[j+1]
            elif j == l:
                res[j] = pref[j-1]
            else:
                res[j] = pref[j-1]*suff[j+1]

        return res


            

        