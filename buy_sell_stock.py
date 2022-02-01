
# prices = [7, 1, 5, 3, 6, 4]
# max_profit = 5

# Left = buy and right = sell
# left = 7, right = 1 # if right is less than left -> set left == to right and move right to the next day
# left = 1, right = 5 # if left is < right -> figure the profit -> we can check if its the max_profit
# WE want to increment right to see if we can sell at a higher price. ++
# Iter thru the entire list once which would gives a O(N) time complexity
# space O(1)

def max_profit(prices):
    left,right = 0, 1
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right

        right += 1

    return max_profit

prices = [7, 1, 5, 3, 6, 4]

ans = max_profit(prices)

print(ans)