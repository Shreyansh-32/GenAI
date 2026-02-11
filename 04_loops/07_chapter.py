flavors = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavors:
    if flavor == "Out of stock":
        continue
    if flavor == "Discontinued":
        break
    print(f"Flavor {flavor}")
print(f"Outside loop")