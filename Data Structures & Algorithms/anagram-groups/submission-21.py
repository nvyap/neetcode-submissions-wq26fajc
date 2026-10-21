class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}
        for i in strs:
            s = [0]*26
            for j in i:
                o = ord(j)-ord('a')
                s[o] += 1
            s = tuple(s)
            if s not in hm:
                hm[s] = []
            hm[s].append(i)

        return list(hm.values())

        