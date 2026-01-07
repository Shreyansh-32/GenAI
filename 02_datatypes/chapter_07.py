# Tuples
# Immutable can't be changed once declared
masala_spices = ("cardamom", "cloves", "cinnamon")
(spice1, spice2, spice3) = masala_spices

print(f"Masala spices : {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2,3
print(f"Ginger ratio : {ginger_ratio}")
print(f"Cardamom ratio : {cardamom_ratio}")

# Swapping
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ginger ratio : {ginger_ratio}")
print(f"Cardamom ratio : {cardamom_ratio}")

# Membership operation

print(f"Is ginger in masala spices? :{'ginger' in masala_spices}")
print(f"Is cardamom in masala spices? :{'cardamom' in masala_spices}")