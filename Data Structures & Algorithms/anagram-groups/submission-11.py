class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for i in strs:
            ord_lst = [0]*26
            for j in i:
                ord_lst[ord(j) - ord('a')] += 1
            
            hm[tuple(ord_lst)].append(i) 
        return list(hm.values())
        