class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        for i in s:
            while i in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(i)
            ln = len(char_set)
            max_len = max(max_len, ln)
        return max_len

        