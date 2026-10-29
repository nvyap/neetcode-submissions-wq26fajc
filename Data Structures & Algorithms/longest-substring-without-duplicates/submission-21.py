class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        seen = set()
        max_len = 0
        for i in s:
            while i in seen:
                seen.remove(queue.popleft())
            queue.append(i)
            seen.add(i)
            l = len(queue)
            max_len = max(max_len,l)
        return max_len

        