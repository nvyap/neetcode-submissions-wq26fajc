class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm_rev = {}
        l = len(nums)
        result = []

        for i in nums:
            hm[i] = hm.get(i,0)+1

        

        for j in hm:
            if hm[j] not in hm_rev:
                hm_rev[hm[j]] = []
            hm_rev[hm[j]].append(j)
        
        for a in range(l,0,-1):
            if a in hm_rev:
                
                result.extend(hm_rev[a])
        return result[:k]


        


        