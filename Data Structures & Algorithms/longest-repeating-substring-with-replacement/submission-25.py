class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        maxf = 0
        char_map = {}
        l = 0
        for r in range(len(s)):
            char_map[s[r]] = char_map.get(s[r],0)+1
            maxf = max(maxf,char_map[s[r]])
            if (r-l+1)-maxf>k:
                char_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, (r-l+1))
        return max_len
