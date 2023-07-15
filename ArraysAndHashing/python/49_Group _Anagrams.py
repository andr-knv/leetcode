from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs:
            counter = [0]*26
            for char in s:
                counter[ord(char)-ord('a')] += 1
            ans[tuple(counter)].append(s)
        return ans.values()
