class Solution:
    def maxBorder(self, w):
        n = len(w)
        f = [0] * n
        for i in range(n):
            k = 1
            while i + k < n and i > w[i + k]:
                k += 1
            f[i] = k
        return f

    def dupsInRange(self, s):
        n = len(s)
        p = [-1] * n
        pd = {}
    
        for i in range(n):
            if s[i] in pd and pd[s[i]] < i:
                p[i] = pd[s[i]]
            pd[s[i]] = i
    
        return p
            
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        u = self.dupsInRange(s)
        ls = self.maxBorder(u)
        return max(ls)
