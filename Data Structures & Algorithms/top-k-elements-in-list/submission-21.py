class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm1 = {}
        hm2 = {}
        res = []

        for i in range(len(nums)):
            hm1[nums[i]] = hm1.get(nums[i],0)+1
        
        for ind,val in hm1.items():
            if val not in hm2:
                hm2[val] = []
            hm2[val].append(ind)
        print(hm2)
        for j in range(len(nums),0,-1):
            if j in hm2 and len(res)<k:
                res += hm2[j]
        return res


                
            


        

        
        
            
        
