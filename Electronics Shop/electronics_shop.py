def getMoneySpent(keyboards, drives, b):
    prices = [k + d for k in keyboards for d in drives if k + d <= b]
    if len(prices) > 0:
        return max(prices)
    else:
        return -1
