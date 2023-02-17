var maxProfit = function (prices) {
  let left = 0;
  let right = 1;
  let currentProfit = 0;
  let maxProfit = 0;

  while (right < prices.length) {
    if (prices[left] < prices[right]) {
      currentProfit = prices[right] - prices[left];
      if (currentProfit > maxProfit) {
        maxProfit = currentProfit;
      }
    } else {
      left = right;
    }
    right++;
  }
  return maxProfit;
};
