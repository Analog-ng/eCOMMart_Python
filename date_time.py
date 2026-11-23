from datetime import date, datetime, timedelta

current_date = date.today()
current_datetime = datetime.now()
future_date = current_date + timedelta(days=30)

# print("Current Date:", current_date)
# print("Current Date and Time:", current_datetime)
# print("Future Date (30 days from now):", future_date)

from datetime import date

# Specific date
order_date = date(2024, 12, 1)
today = date.today()
order_placed = datetime(2024, 12, 1, 14, 30, 0)
now = datetime.now()
order_date = date(2024, 12, 1)

# print(order_date.strftime("%d-%m-%Y"))
# print(order_date.strftime("%B %d, %Y"))
# print(order_date.strftime("%d %b %Y"))
# print(f"Order placed on: {order_date.strftime('%d %B %Y')}")
# print(f"Day of week: {order_date.strftime('%A')}")
# print(now) 
# print(order_placed)
# print(order_date)
# print(today)

order_date    = date(2024, 12, 1)

# Add days — calculate delivery date
delivery_date = order_date + timedelta(days=3)
print(delivery_date)



