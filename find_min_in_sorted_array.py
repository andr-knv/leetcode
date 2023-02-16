def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    result = nums[0]
  
    while left <= right:
        if nums[left] < nums[right]:
            result = min(nums[left], result)
            break
        middle = (left + right) // 2
        
        if nums[middle] >= nums[left]:
            left = middle + 1
        else:
            right = middle - 1
        result = min(result, nums[middle])
        
    return result

