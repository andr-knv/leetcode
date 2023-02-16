def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Time limit exceeded solution

    i, j, k = 0, 1, 2
    result = []
    nums.sort() 
        
    while i < len(nums) - 1:
        if nums[i] > 0:
            i += 1
        j = i + 1
        k = len(nums)-1
        while j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] == 0:
                if [nums[i], nums[j], nums[k]] not in result:
                    result.append([nums[i], nums[j], nums[k]])
                j += 1
        i += 1   
    return result
    """

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
