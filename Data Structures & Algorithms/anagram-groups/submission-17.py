class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        if len(strs) == 0:
            return [[""]]

        for i in strs:
            char_count = [0]*26
            for j in i:
                o = ord(j) - ord('a')
                char_count[o] += 1
            cc = tuple(char_count)
            if cc not in hm:
                hm[cc] = []
            hm[cc].append(i)
        return list(hm.values())
        
            
            

        