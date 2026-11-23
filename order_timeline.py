from datetime import date, datetime, timedelta

#full order timeline

order_date = date(2024, 12, 1)
delivery_date = order_date + timedelta(days=3)
return_date = delivery_date + timedelta(days=7)
today = datetime.now().date()

days_since_order = (today - order_date).days
can_return = today <= return_date   

# print(f"Order Date: {order_date.strftime('%d %B %Y')}")
# print(f"Delivery Date: {delivery_date.strftime('%d %B %Y')}")
# print(f"Return Date: {return_date.strftime('%d %B %Y')}")
# print(f"Days Since Order: {days_since_order}")
# print(f"Can Return: {can_return}")


ecommart_raw_date = "2024-12-01"

format1 = ecommart_raw_date.replace("-", "/")
# format2 = datetime.strptime(ecommart_raw_date, "%Y-%m-%d").strftime("%d %B %Y")  # This line will raise an error because ecommart_raw_date is a string, not a date object.

                                     

print(f"Formatted Date: {format1}")
# print(f"Formatted Date: {format2}")