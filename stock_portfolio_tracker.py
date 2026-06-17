print("========= STOCK PORTFOLIO TRACKER =======")
stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGLE" :140,
    "MSFT" : 320,
    "AMZN" : 150,
    "NFLX" : 400,
    "META" :300
    }
portfolio = {}
total_investment = 0
print("\nAvailable Stocks and Prices:\n")
for stock, price in stock_prices.items():
    print(stock, "=", "$" , price)

print("\nEnter stock details to calculate investment.")
print("Type 'done' when finished.\n")

while True:
    stock_name = input("Enter Stock Name: ").upper()
    if stock_name =="DONE":
        break
    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))

        stock_value = stock_prices[stock_name] * quantity
        
        #Store in dictionary
        portfolio[stock_name] = {
            "Price": stock_prices[stock_name],
            "Quantity": quantity,
            "Total": stock_value
            }
        #Add to total investment
        total_investment += stock_value
        
        print(stock_name, "added sucessfully!\n")
        
    else:
        print("stock not available in database.\n")
        
#Display Portfolio Summary
print("\n====== PORTFOLIO SUMMARY ======\n")
 
for stock, details in portfolio.items():
     print("Stock Name :", stock)
     print("Price      : $", details["Price"])
     print("Quantity   :", details["Quantity"])
     print("Investment : $",details["Total"])
     print("----------------------------------")
#Display total investment
print("\nTotal Investment Value = $", total_investment)

#Find highest investment stock
highest_stock = ""
highest_value = 0

for stock, details in portfolio.items():
     if details["Total"] > highest_value:
         highest_value = details["Total"]
         highest_stock =stock
 #Display highesgt investment
         if highest_stock != "":
             print("\nHighest Investment Stock :", highest_stock)
             print("Highest Investment Value : $", highest_value)
     # Bonus Feature
     print("\n====== EXTRA ANALYSIS ======")

     number_of_stock = len(portfolio)

     print("Total Different Stocks Purchased :", number_of_stocks)

     if number_of_stocks > 0:

         average_investment = total_investment / number_of_stocks
         print("Average Investment per stock = $", average_investment)

         print("\nThank You for Using Stock Portfolio Tracker!")







                                  
