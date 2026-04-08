class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        count_rev = {}
        res = []
        for i in nums:
            counts[i] = counts.get(i,0)+1

        for ind,val in counts.items():
            if val not in count_rev:
                count_rev[val] = []
            count_rev[val].append(ind)

        for n in range(len(nums),0,-1):
            if n in count_rev and len(res)<k:
                res += count_rev[n]
        
        return res



            

        