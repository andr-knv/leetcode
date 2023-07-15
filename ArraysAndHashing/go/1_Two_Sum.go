func twoSum(nums []int, target int) []int {
    hashMap := make(map[int]int)

	for i, num := range nums {
		_, ok := hashMap[num]
		if ok {
			return []int{i, hashMap[num]}
		}
		hashMap[target-num] = i
	}
	return nil
    
}