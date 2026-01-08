# Set

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

print(f"Essential spices : {essential_spices}")
print(f"Optional spices : {optional_spices}")
print(f"Intersection : {essential_spices & optional_spices}")
print(f"Union : {essential_spices | optional_spices}")
print(f"Only in essential spices: {essential_spices - optional_spices}")
# Membership operator
print(f"Is cloves in essential spices? : {'cloves' in essential_spices}")
print(f"Is cloves in optional spices? : {'cloves' in optional_spices}")