class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in strs:
            ord_lst = [0]*26
            for j in i:
                ind = ord(j) - ord('a')
                ord_lst[ind] += 1
            if tuple(ord_lst) not in hm:
                hm[tuple(ord_lst)] = []
            hm[tuple(ord_lst)].append(i) 
        return list(hm.values())
        