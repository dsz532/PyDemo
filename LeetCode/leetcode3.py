class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        rk, ans = 0, 0
        n = len(s)
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk < n and s[rk] not in occ:
                occ.add(s[rk])
                rk += 1
            ans = max(ans, rk - i)
        return ans

    pass


s = "ohomm"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
