customer_name = "John Doe"
order_id = "ORD12345"
itemlist = ["Wireless Mouse", "USB Hub Mouse", "Keyboard", "Monitor", "Webcam"]

print(f"""
    ===========================================
        eCOMMart — Order Confirmation
    ===========================================
    Customer : {customer_name}
    Order ID : {order_id}
    Items    : {', '.join(itemlist)}
    Status   : Payment Confirmed

    Thank you for shopping at eCOMMart!
    Your order will be delivered in 2-3 days.
    ===========================================
""")

item1 = 299.99
item2 = 199.00
item3 = 849.00
item4 = 499.00
item5 = 150.00

subtotal = item1 + item2 + item3 + item4 + item5

tax_rate = 0.18
tax_amount = subtotal * tax_rate
new_total = subtotal + tax_amount

if subtotal > 500:
    discount = 50
    discount_amount = subtotal - discount
    new_total = discount_amount + tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"New Total: ${new_total:.2f}")