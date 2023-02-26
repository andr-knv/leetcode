const characterReplacement = function (s, k) {
  let [left, result, highestFreq, counts] = [0, 0, 0, new Map()];

  for (let right = 0; right < s.length; right++) {
    let rightChar = s.charAt(right);
    counts[rightChar] = counts[rightChar] + 1 || 1;

    highestFreq = Math.max(highestFreq, counts[rightChar]);

    if (right - left + 1 - highestFreq > k) {
      let leftChar = s.charAt(left);
      counts[leftChar] -= 1;
      left++;
    }

    result = Math.max(result, right - left + 1);
  }
  return result;
};
