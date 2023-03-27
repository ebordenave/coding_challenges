# Define a function called "maxProfit" that takes a list of integers called "prices" as input and returns an integer.
def maxProfit(self, prices: list[int]) -> int:
    # Set initial values for the minimum price and maximum profit to infinity and zero, respectively.
    min_price = float('inf')
    max_profit = 0
    # Iterate through each price in the list of prices.
    for price in prices:
        # If the current price is lower than the current minimum price, update the minimum price.
        if price < min_price:
            min_price = price
        # Otherwise, calculate the profit that would be made by selling at the current price
        # and update the maximum profit seen so far if it's higher than the previous maximum.
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    # Return the maximum profit seen.
    return max_profit

prices = [7,1,5,3,6,4]

maxProfit(prices)
