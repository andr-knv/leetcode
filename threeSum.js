const threeSum = function (nums) {
  let result = [];
  nums.sort(function (a, b) {
    return a - b;
  });

  for (let [idx, val] of nums.entries()) {
    if (idx > 0 && val === nums[idx - 1]) {
      continue;
    }

    let left = idx + 1;
    let right = nums.length - 1;

    while (left < right) {
      if (val + nums[left] + nums[right] > 0) {
        right--;
      } else if (val + nums[left] + nums[right] < 0) {
        left++;
      } else {
        result.push([val, nums[left], nums[right]]);
        left++;
        while (nums[left] === nums[left - 1] && left < right) {
          left++;
        }
      }
    }
  }
  return result;
};
