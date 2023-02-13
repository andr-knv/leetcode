var longestConsecutive = function (nums) {
  if (nums.length < 1) {
    return 0;
  }
  nums = nums.sort(function (a, b) {
    return a - b;
  });
  let sum = 1;
  let results = [];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] - 1 === nums[i - 1]) {
      sum++;
    } else if (nums[i] === nums[i - 1]) {
      sum = sum;
    } else {
      results.push(sum);
      sum = 1;
    }
  }
  results.push(sum);
  return Math.max(...results);
};
