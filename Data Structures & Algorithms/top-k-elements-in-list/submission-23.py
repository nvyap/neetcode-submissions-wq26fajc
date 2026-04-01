class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm1 = {}
        hm2 = {}
        res = []
        a = 0

        for ind,val in enumerate(nums):
            hm1[val] = hm1.get(val,0)+1

        for j,l in hm1.items():
            if l not in hm2:
                hm2[l] = []
            hm2[l].append(j)
        
        print(hm2)

        for n in range(len(nums),0,-1):
            if n in hm2 and len(res)<k:
                res += hm2[n]
        return res
        

        
       


                
            


        

        
        
            
        
