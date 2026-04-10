class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for i in strs:
            ind = [0]*26
            for j in i:
                ind[ord(j)-ord('a')] += 1
            hm[tuple(ind)].append(i)
        return list(hm.values())
            
            

        