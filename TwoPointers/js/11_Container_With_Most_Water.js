var maxArea = function(height) {
    let left = 0;
  let right = height.length - 1;
  let _maxArea = 0;

  while (left < right) {
    let area = Math.min(height[left], height[right]) * (right - left);

    if (height[left] > height[right]) {
      right--;
    } else {
      left++;
    }
    _maxArea = Math.max(area, _maxArea);
  }

  return _maxArea;
};