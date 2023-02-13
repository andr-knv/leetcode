def longest_consecutive(nums: list[int]) -> int:
    if len(nums) < 1:
            return 0
    nums.sort()
    sum = 1
    results = []
    for i in range(1, len(nums)):
        if nums[i] - 1 == nums[i-1] :
            sum += 1
        elif nums[i] == nums[i-1]:
            sum = sum
        else:
            results.append(sum)
            sum = 1
    results.append(sum)
    return max(results) 

