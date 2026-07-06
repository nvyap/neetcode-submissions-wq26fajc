class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hm = defaultdict(list)
        for i in strs:
            char_count = [0]*26
            for j in i:
                ordinality = ord(j) - ord('a')
                char_count[ordinality] += 1
            cc = tuple(char_count)
            if cc not in strs_hm:
                strs_hm[cc] = []
            strs_hm[cc].append(i)
        return list(strs_hm.values())

            

        