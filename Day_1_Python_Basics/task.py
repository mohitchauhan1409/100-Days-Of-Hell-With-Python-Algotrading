# program to calculate the average of price of stocks in a week.

day1_price = int(input("Enter day1 stock price: "))
day2_price = int(input("Enter day2 stock price: "))
day3_price = int(input("Enter day3 stock price: "))
day4_price = int(input("Enter day4 stock price: "))
day5_price = int(input("Enter day5 stock price: "))
day6_price = int(input("Enter day6 stock price: "))
day7_price = int(input("Enter day7 stock price: "))
week_average = (day1_price+ day2_price+ day3_price+ day4_price+ day5_price+ day6_price+ day7_price) / 7
print("Average stock price of the week is", week_average)