from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        tmp = {}
        answer = []
        for num in nums:
            tmp[num] = 1 + tmp.get(num, 0)
        answer = sorted(tmp.items(), key=lambda x: x[1], reverse=True)[:k]
        return [i[0] for i in answer]


class SingleLineSolution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [i[0] for i in Counter(nums).most_common(k)]
