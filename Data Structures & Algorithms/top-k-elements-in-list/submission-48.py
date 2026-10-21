class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm_rev = {}

        for i in nums:
            hm[i] = hm.get(i,0)+1
        
        for j in hm:
            if hm[j] not in hm_rev:
                hm_rev[hm[j]] = []
            hm_rev[hm[j]].append(j)
        
        l = len(nums)
        result = []
        for n in range(l,0,-1):
            if n in hm_rev:
                result.extend(hm_rev[n])
        
        return result[:k]
        