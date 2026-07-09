class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        #n = int(n)
        while n != 0:
            s += n%2
            n = n//2
        return int(s)
        