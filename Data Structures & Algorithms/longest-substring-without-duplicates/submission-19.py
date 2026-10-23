class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        ind = 0
        max_len = 0
        for i in s:
            while i in char_set:
                char_set.remove(s[ind])
                ind += 1
            char_set.add(i)
            max_len = max(max_len,len(char_set))
        return max_len


        