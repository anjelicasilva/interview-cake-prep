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