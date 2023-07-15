func twoSum(numbers []int, target int) []int {
    left, right := 0, len(numbers)-1

    for numbers[left] + numbers[right] != target{
        if left > right{
            return nil
        }
        if numbers[left] + numbers[right] > target{
            right--
        }else{
            left++
        }
    }
    left++
    right++
    return []int{left, right}
}