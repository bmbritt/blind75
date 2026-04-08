class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = 0
        sell = 1
        
        while sell < len(prices):
            # if would lose money, just buy it cheaper
            if (prices[sell] <= prices[buy]):
                buy = sell
            else:
                result = max(result, prices[sell] - prices[buy])
            sell += 1
        return max(0, result)
                
            