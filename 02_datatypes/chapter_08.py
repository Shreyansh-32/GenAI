# List

ingredients = ["ginger", "cloves", "cinammon"]

print(f"Ingredients : {ingredients}")
ingredients.append("cardamom")
print(f"Ingredients : {ingredients}")
ingredients.insert(2, "milk")
print(f"Ingredients : {ingredients}")

last_ingredient = ingredients.pop()
print(f"Last ingredient : {last_ingredient}")
print(f"Ingredients : {ingredients}")

ingredients.sort()
print(f"Ingredients : {ingredients}")

ingredients.reverse()
print(f"Ingredients : {ingredients}")

sugar_level = [1,2,3,4,5]
print(f"Maximum sugar level : {max(sugar_level)}")
print(f"Minimum sugar level : {min(sugar_level)}")