# https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def say(s):
            result = ""
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result += str(count) + s[i - 1]
                    count = 1
            result += str(count) + s[-1] # last elemnt
            return result

        res = "1"
        for _ in range(n - 1):
            res = say(res)

        return res
