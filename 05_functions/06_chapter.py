def serve_chai():
    chai_type = "Masala" #Local scope
    print(f"Your {chai_type} chai is ready from fn!")

chai_type = "Lemon" #Gloabl scope
serve_chai()
print(f"Your {chai_type} chai is ready from outer!")

def chai_counter():
    chai_order = "Lemon" #Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print(f"Inner : {chai_order}")
    print_order()
    print(f"Outer : {chai_order}")

chai_counter()