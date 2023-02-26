const twoSum = function (numbers, target) {
  let left = 0;
  let right = numbers.length - 1;
  while (numbers[left] + numbers[right] !== target) {
    if (left > right) {
      return -1;
    }
    if (numbers[left] + numbers[right] > target) {
      right--;
    } else {
      left++;
    }
  }
  left++;
  right++;
  return [left, right];
};
