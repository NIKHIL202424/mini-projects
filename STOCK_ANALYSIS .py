
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_value = 0

file = open("portfolio.txt", "w")

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_value += value

        print(f"{stock}: RS.{value}")
        file.write(f"{stock} - Quantity: {quantity}, Value: RS.{value}\n")
    else:
        print("Stock not found!")

print("Total Portfolio Value: RS.", total_value)
file.write(f"\nTotal Portfolio Value: RS.{total_value}")

file.close()

print("Portfolio saved to portfolio.txt")
