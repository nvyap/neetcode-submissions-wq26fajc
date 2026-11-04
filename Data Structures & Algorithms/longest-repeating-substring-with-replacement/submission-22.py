class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        max_len = 0
        char_set = {}
        l = 0
        for r in range(len(s)):
            char_set[s[r]] = char_set.get(s[r],0)+1
            maxf = max(maxf,char_set[s[r]])
            if (r-l+1)-maxf>k:
                char_set[s[l]] -= 1
                l += 1
            max_len = max(max_len, (r-l+1))
        return max_len

        