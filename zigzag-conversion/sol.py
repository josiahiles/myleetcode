import unittest
class Solution:
    def zzFnc(self, n, m) -> int:
        assert m >= 1
        if m == 1: return 0
        pid = 2 * (m - 1)
        pos = n % pid
        return min(pos, pid - pos)
    def convert(self, s: str, numRows: int) -> str:
        N = numRows
        dic = {m: [] for m in range(N)}
        for i, c in enumerate(s):
            dic[self.zzFnc(i, N)].append(c)
        sol = []
        for key in dic:
            sol.append("".join(dic[key]))
        return "".join(sol)
class test(unittest.TestCase):
    sol = Solution()
    def test1(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
    def test2(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
if __name__ == '__main__':
    unittest.main()









