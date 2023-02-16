const findMin = function (nums) {
  let result = nums[0];
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    if (nums[left] < nums[right]) {
      result = Math.min(nums[left], result);
      break;
    }
    let middle = Math.floor((left + right) / 2);

    if (nums[middle] >= nums[left]) {
      left = middle + 1;
    } else {
      right = middle - 1;
    }

    result = Math.min(result, nums[middle]);
  }
  return result;
};
