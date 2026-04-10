class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # Shrink from left while duplicate exists
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add current character
            char_set.add(s[r])
            len_set  = len(char_set)
            # Update max length
            max_len = max(max_len, len_set)
        
        return max_len