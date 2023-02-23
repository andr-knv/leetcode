def twoSum(numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if left > right:
                return -1
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        left += 1
        right += 1
        return[left, right]
