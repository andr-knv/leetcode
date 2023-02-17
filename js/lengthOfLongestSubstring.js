const lengthOfLongestSubstring = function (s) {
  let left = 0;
  let sum = 0;
  let seen = new Set();

  for (let right = 0; right < s.length; right++) {
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }
    seen.add(s[right]);

    if (right - left + 1 > sum) {
      sum = right - left + 1;
    }
  }
  return sum;
};
