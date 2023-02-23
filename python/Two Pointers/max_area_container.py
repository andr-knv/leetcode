def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    _max_area = 0

    while left < right:
        area = (min(height[left], height[right])) * (right - left)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
        _max_area = max(area, _max_area)

    return _max_area



