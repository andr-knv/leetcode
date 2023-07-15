class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = (min(height[left], height[right])) * (right - left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            max_area = max(area, max_area)

        return max_area