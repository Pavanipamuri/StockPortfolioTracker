# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0
portfolio_summary = ""

print("📈 Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))

        stock_value = stock_prices[stock_name] * quantity
        total_investment += stock_value

        portfolio_summary += (
            f"{stock_name} - Quantity: {quantity}, "
            f"Price: ${stock_prices[stock_name]}, "
            f"Total: ${stock_value}\n"
        )

        print(f"✅ Added {stock_name} to portfolio.")

    except ValueError:
        print("⚠ Please enter a valid number.")

# Display Results
print("\n📊 Portfolio Summary")
print(portfolio_summary)

print(f"💰 Total Investment Value: ${total_investment}")

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")
    file.write(portfolio_summary)
    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n✅ Portfolio saved to portfolio.txt")