# chai_type = "Ginger"

# def print_order(type):
#     print(f"Your {type} chai is ready!")

# print_order(chai_type)

#Also called as the parameter
def chai_counter(type, milk, sweetness):
    print(f"Your {type} chai is ready with {milk} milk and {sweetness} sweetness")

chai_counter(sweetness="low", type="masala", milk="low")

#Also called as the args and keyword args
def print_order(*ingredients, **extras):
    print("Ingredients : ",ingredients)
    print("Extras : ",extras)

print_order("Cinnamon", "Cardamom", sweetner = "low", milk = "Yes")