class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for i in strs:
            l = [0]*26
            for j in i:
                l[ord(j)-ord('a')] += 1
            hm[tuple(l)].append(i)
        
        return list(hm.values())


        