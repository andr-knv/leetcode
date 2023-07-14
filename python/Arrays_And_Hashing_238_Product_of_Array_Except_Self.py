class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1]

        for i in range(1, len(nums)):
            ans.append(ans[-1] * nums[i-1])

        s = 1

        for i in range(len(nums)-2, -1, -1):
            s *= nums[i+1]
            ans[i] *= s
        return ans
