class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize max_profit to 0, as no profit is made yet
        # Initialize min_price to a very large number (infinity)
        # So first price encountered will become initial price definitely
        max_profit = 0
        min_price = float('inf') # A common way to represent large number infinity

        # Iterate through each price in given array
        for price in prices:

            # start with first price in array as min_price
            # update 'min_price' to new lowest price every time we iterate to next value

            min_price = min(min_price, price)

            # keeps track of current profit in every iteration
            current_profit = price - min_price 

            # Updates max_profit to max value
            max_profit = max(max_profit, current_profit)

        return max_profit
            
