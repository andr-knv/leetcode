class Solution:
    def best_time_to_buy_and_sell(prices: list[int]) -> int:
        left = 0
        right = 1 
        current_profit, max_profit = 0, 0
        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                if current_profit > max_profit:
                    max_profit = current_profit
            else:
                left = right
            right += 1
        return max_profit

        

    





