order_amount = int(input("Amount of order : "))

final_statement = "Free delivery" if order_amount > 300 else "Delivery fees Rs.30"
print(final_statement)