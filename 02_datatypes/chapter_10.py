# Dictionary

chai_order = dict(type="masala", sugar = 2, base="black tea")
print(f"Chai order: {chai_order}")

chai_ingredients = {"base" : "black tea", "sugar":2, "ginger":True, "cloves":False}
print(f"Chai ingredients: {chai_ingredients['base']} {chai_ingredients['sugar']}")

is_cloves = chai_ingredients.get("cloves", "Not present")
print(f"Cloves in chai? : {is_cloves}")


del chai_ingredients["cloves"]
print(f"Chai ingredients : {chai_ingredients}")

is_cloves = chai_ingredients.get("cloves", "Not present")
print(f"Cloves in chai? : {is_cloves}")