# chai_type = "Ginger"

# def print_order(type):
#     print(f"Your {type} chai is ready!")

# print_order(chai_type)

def chai_counter(type, milk, sweetness):
    print(f"Your {type} chai is ready with {milk} milk and {sweetness} sweetness")

chai_counter(sweetness="low", type="masala", milk="low")

def print_order(*ingredients, **extras):
    print("Ingredients : ",ingredients)
    print("Extras : ",extras)

print_order("Cinnamon", "Cardamom", sweetner = "low", milk = "Yes")