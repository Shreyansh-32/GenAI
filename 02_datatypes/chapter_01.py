sugar_amount = 2
print(f"Amount of sugar: {sugar_amount}")
print(f"ID of 2 : {id(2)}")
print(f"ID of 12 : {id(12)}")

sugar_amount = 12
print(f"Amount of sugar:{sugar_amount}")
print(f"ID of 2 : {id(2)}")
print(f"ID of 12 : {id(12)}")

# 2 and 12 are immutable since its memory location doesn't change
# Although reference of sugar_amount changes which is mutable