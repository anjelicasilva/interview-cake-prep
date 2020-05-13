# Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

# My Attempt

def get_max_profit(stock_prices):
            
    buy_idx = 0
    sell_idx = 1
    profit = stock_prices[sell_idx]-stock_prices[buy_idx]
    
    for i in range(1, len(stock_prices)):
        if (i > buy_idx) and ((stock_prices[i] - stock_prices[buy_idx]) > profit):
            sell_idx = i
        if (i < sell_idx) and ((stock_prices[sell_idx] - stock_prices[i]) > profit):
            buy_idx = i
    
    return stock_prices[sell_idx]-stock_prices[buy_idx]


# IC Solution

def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)
    
    return max_profit