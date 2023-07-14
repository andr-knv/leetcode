class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class SingleLineSolution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not len(set(nums)) == len(nums)
