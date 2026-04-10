class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_sort = sorted(nums)
        if nums_sort[0]>0: return []
        
        for i in range(len(nums_sort)):
            if i > 0 and nums_sort[i] == nums_sort[i-1]: continue
            j = i+1
            k = len(nums_sort)-1
            n1 = nums_sort[i]*-1

            while j < k:
                if nums_sort[j] + nums_sort[k] < n1:
                    j += 1
                elif nums_sort[j] + nums_sort[k] >n1:
                    k -= 1
                elif i!=k and j!=k and [nums_sort[i],nums_sort[j],nums_sort[k]] not in res:
                    res.append([nums_sort[i],nums_sort[j],nums_sort[k]])
                else: 
                    k -= 1
                    j += 1
        return res
