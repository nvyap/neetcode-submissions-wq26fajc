class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for i in strs:
            ordi = [0]*26
            for j in i:
                ind = ord(j) - ord('a')
                ordi[ind] += 1
            #if tuple(ordi) not in hm:
            #    hm[ordi] = []
            hm[tuple(ordi)].append(i)
        return list(hm.values())      