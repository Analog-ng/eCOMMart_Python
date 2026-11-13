# eCOMMart Product Catalog Entry

product_name_1 = "Wireless Mouse"
brand = "TechPro"
price_1 = 499.00
is_in_stock = True
category, seller_city = "Electronics", "Lagos"

product_name_2 = "USB Hub Mouse"
brand = "TechPro"
price_2 = 350.00
is_in_stock = True
category, seller_city = "Electronics", "Lagos"

# print(f"# eCOMMart Product Catalog Entry")
# print(f"Product: {product_name}")
# print(f"Brand: {brand}")    
# print(f"Price: ${price:.2f}")
# print(f"Category: {category}")
# print(f"Seller City: {seller_city}")

# total_price = price_1 + price_2
# difference = price_1 - price_2
# average_price = total_price / 2
# bulk_cost = price_1 * 10 
# remainder = total_price % 100
# tax = price_1 * 0.18 
# per_unit_cost = total_price // 2

# print(f"Total Price: ${total_price:.2f}")
# print(f"Difference: ${difference:.2f}")
# print(f"Average Price: ${average_price:.2f}")
# print(f"Bulk Cost (10 units): ${bulk_cost:.2f}")
# print(f"Remainder when divided by 100: ${remainder:.2f}")
# print(f"Tax (18%): ${tax:.2f}")
# print(f"Per Unit Cost: ${per_unit_cost:.2f}")


new_product_name = input("Enter the name of the new product: ")
new_product_price = float(input("Enter the price of the new product: "))
new_product_category = input("Enter the category of the new product: ")
new_product_seller_city = input("Enter the seller's city: ")
discounted_price = new_product_price * 0.2
latest_price = new_product_price - discounted_price

print(f"# eCOMMart New Product Entry")
print(f"Product: {new_product_name}")  
print(f"Price: ${new_product_price:.2f}")
print(f"Discount: {discounted_price:.2f}")
print(f"Latest Price: ${latest_price:.2f}")
print(f"Category: {new_product_category}")
print(f"Seller City: {new_product_seller_city}")



