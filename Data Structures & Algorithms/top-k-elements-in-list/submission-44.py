class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm_rev = {}
        res = []
        for i in nums:
            hm[i] = hm.get(i,0)+1
        for j in hm:
            if hm[j] not in hm_rev:
                hm_rev[hm[j]] = []
            hm_rev[hm[j]].append(j)
        
        l = len(nums)
        while l>0 and len(res)<k:
            if l in hm_rev:
                res.extend(hm_rev[l])
            l -= 1
        return res[:k]



        