def chai_counter():
    chai_type = "Masala"
    def print_order():
        nonlocal chai_type
        chai_type = "Kesar"
    print_order()
    print(f"Your order for {chai_type} chai is ready!")

chai_counter()