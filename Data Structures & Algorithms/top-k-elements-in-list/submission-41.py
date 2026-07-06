class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hm = {}
        hm_rev = defaultdict()
        res = []
        for i in nums:
            freq_hm[i] = freq_hm.get(i,0)+1
        
        for j in freq_hm:
            if freq_hm[j] not in hm_rev:
                hm_rev[freq_hm[j]] = []
            hm_rev[freq_hm[j]].append(j)


        for n in range(len(nums),0,-1):
            if n in hm_rev:
                res.extend(hm_rev[n])
        
        return res[:k]
