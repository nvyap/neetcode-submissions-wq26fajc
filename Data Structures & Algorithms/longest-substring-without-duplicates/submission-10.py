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
            # Update max length
            max_len = max(max_len, r - l + 1)
        
        return max_len