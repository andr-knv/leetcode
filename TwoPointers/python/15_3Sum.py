class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx-1]:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                if val + nums[left] + nums[right] > 0:
                    right -= 1
                elif val + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result