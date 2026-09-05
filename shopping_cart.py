customer_name = input("Enter customer name: ")
product1_name = input("Enter product 1 name: ")
product1_price = float(input(f"Enter price for {product1_name}: "))
product2_name = input("Enter product 2 name: ")
product2_price = float(input(f"Enter price for {product2_name}: "))
product3_name = input("Enter product 3 name: ")
product3_price = float(input(f"Enter price for {product3_name}: "))

subtotal = product1_price + product2_price + product3_price
if subtotal >= 5000:
    discount_percentage = 20
elif subtotal >= 3000:
    discount_percentage = 10
elif subtotal >= 1000:
    discount_percentage = 5
else:
    discount_percentage = 0
discount_amount = subtotal *(discount_percentage /100)

amount_after_discount = subtotal - discount_amount
tax_amount = (amount_after_discount * 5) /100
final_total = amount_after_discount + tax_amount
print("\n-- Shopping Recipt ---")
print(f"Customer name: {customer_name}")
print(f"{product1_name}: ${product1_price:.2f}")
print(f"{product2_name}: ${product2_price:.2f}")
print(f"{product3_name}: ${product3_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount ({discount_percentage}%): ${discount_amount:.2f}")
print(f"Amount after discount: ${amount_after_discount:.2f}")
print(f"Tax (5%): ${tax_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")