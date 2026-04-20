class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            char_count = [0]*26
            for j in i:
                o = ord(j) - ord('a')
                char_count[o] += 1
            anagrams[tuple(char_count)].append(i)
        return list(anagrams.values())
        