class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = deque()
        seen_set = set()
        max_len = 0
        for i in s:
            while i in seen_set:
                seen_set.remove(seen.popleft())
            seen.append(i)
            seen_set.add(i)
            max_len = max(max_len, len(seen))
        return max_len
        