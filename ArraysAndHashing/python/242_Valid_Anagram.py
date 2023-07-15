from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for idx, _ in enumerate(s):
            if s.count(s[idx]) != t.count(s[idx]):
                return False
        return True


class SingleLineSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
