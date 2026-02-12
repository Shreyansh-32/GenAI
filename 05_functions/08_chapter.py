chai_type = "Plain"

def chai_counter():
    def print_order():
        global chai_type
        chai_type = "Masala"
    print_order()

print(f"Chai type before fn call : {chai_type}")
chai_counter()
print(f"Chai type after fn call : {chai_type}")