class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm_rev = {}
        result = []
        for n in nums:
            hm[n] = hm.get(n,0)+1
        for i in hm:
            if hm[i] not in hm_rev:
                hm_rev[hm[i]] = []
            hm_rev[hm[i]].append(i)
        l = len(nums)
        #print(hm_rev)
        for i in range(l,0,-1):
            if i in hm_rev and len(result)<k:
                #print(l)
                result.extend(hm_rev[i])
        
        return result[:k]
        