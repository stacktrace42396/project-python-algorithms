def max_stock_profit(prices_arr):
	#	takes in array of prices as parameter
	#	returns the max possible profit of the day
	max_profit = -1
	buy_price = 0
	sell_price = 0

	change_buy_price = True

	for i in range(0, len(prices_arr)+1):
		
		if change_buy_price:
			buy_price = prices_arr[i]

		if i+1 < len(prices_arr):
			sell_price = prices_arr[i + 1]
		else:
			break
		
		if sell_price < buy_price:
			change_buy_price = True
		else:
			temp_profit = sell_price - buy_price
			if temp_profit > max_profit:
				max_profit = temp_profit
			change_buy_price = False

	return max_profit


print(max_stock_profit([32, 46, 26, 38, 40, 48, 42]))
print(max_stock_profit([10, 18, 4, 5, 9, 6, 16, 12]))
