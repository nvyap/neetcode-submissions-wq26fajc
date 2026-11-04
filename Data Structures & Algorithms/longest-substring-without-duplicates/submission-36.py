class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = deque()
        seen = set()
        max_len = 0
        for i in s:
            while i in seen:
                seen.discard(stack.popleft())
            stack.append(i)
            seen.add(i)
            max_len = max(max_len, len(stack))
        return max_len

        