class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, val in enumerate(nums):
            res = target-val
            if res in seen:
                return [idx, seen[res]]
            seen[val] = idx
        return
