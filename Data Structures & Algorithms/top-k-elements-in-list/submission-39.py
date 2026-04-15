class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm_rev = {}
        res = []
        l = len(nums)
        for i in nums:
            hm[i] = hm.get(i,0)+1
        
        for ind,val in hm.items():
            if val not in hm_rev:
                hm_rev[val] = []
            hm_rev[val].append(ind)

        for j in range(l,0,-1):
            if j in hm_rev and len(res)<k:
                res.extend(hm_rev[j])
        
        return res[:k]

        