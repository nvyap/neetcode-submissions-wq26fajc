class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm_rev = {}
        res = []

        for i in nums:
            hm[i] = hm.get(i,0)+1

        for ind,val in hm.items():
            if val not in hm_rev:
                hm_rev[val] = []
            hm_rev[val].append(ind)


        for l in range(len(nums),0,-1):
            if l in hm_rev and len(res)<k:
                res += hm_rev[l]
            
        return res
        