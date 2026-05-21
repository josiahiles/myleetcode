class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di = {}
        i = 0
        k = 0
        for j, c in enumerate(s):
            if c in di and di[c] >= i:
                i = di[c] + 1
            di[c] = j
            k = max(k, j - i + 1)
        return k
