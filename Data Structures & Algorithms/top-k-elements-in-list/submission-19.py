class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm2 = {}
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i],0)+1
        res = []
        for ind,val in hm.items():
            if val not in hm2:
                hm2[val] = []
            hm2[val].append(ind)

        for j in range(len(nums),0,-1):
            if j in hm2 and len(res)<k:
                res += hm2[j]
        return res


        
        
            
        
