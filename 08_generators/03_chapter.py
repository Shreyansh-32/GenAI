# Sending value to a yield

def customer_order():
    print("Welcome! What chai would you like to have?")
    order = yield

    while True:
        print(f"Preparing {order} Chai!")
        order = yield

tea_stall = customer_order()
next(tea_stall) #Start generator

tea_stall.send("Masala")
tea_stall.send("Lemon")