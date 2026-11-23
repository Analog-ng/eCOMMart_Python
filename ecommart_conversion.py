# Starting values
price_str     = "1299"     
# string price from a form
qty_float     = 2.0        
# float quantity from an API
in_stock_int  = 1          
# integer flag (1 = in stock)
product_id    = 5001       
# integer used to build a SKU
discount_bool = True       
# boolean discount flag


price_int = int(price_str)
qty_int = int(qty_float)  
in_stock_bool = bool(in_stock_int)
product_sku = f"SKU-{product_id}"
discount_status = float(discount_bool)


