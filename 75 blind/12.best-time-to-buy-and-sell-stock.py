class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            if min_price >= p:
                min_price = p
            else:
                profit = p - min_price
                max_profit = max(max_profit, profit)

        return max_profit
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([2,4,1]))
print(sol.maxProfit([2,1,2,1,0,1,2]))