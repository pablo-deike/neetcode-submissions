class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = len(prices) - 1
        profit = 0
        while r > 0:
            print(r)
            min_val = float("inf")
            min_idx = r
            for idx in range(r):
                if prices[r - idx - 1] > prices[r]:
                    break
                if prices[r - idx - 1] < min_val:
                    min_idx = r - idx - 1
                    min_val = prices[min_idx]
            profit = max(prices[r] - min_val, profit)
            r = min_idx - 1
        return profit