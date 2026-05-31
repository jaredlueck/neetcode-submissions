class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        m = [0] * len(prices)

        curr_max = 0
        for i in range(len(prices)-1, -1, -1):
            print(i)
            curr_max = max(prices[i], curr_max)
            m[i] = curr_max
        print(m)
        for i in range(0, len(prices)-1):
            profit = max(profit, m[i + 1] - prices[i])
        return profit