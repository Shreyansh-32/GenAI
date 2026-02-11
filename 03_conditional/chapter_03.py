cup_size = input("What size of chai would you like small, medium or large? \n").lower()

if cup_size == "small":
    print(f"For a small cup it would be 10Rs")

elif cup_size == "medium":
    print("For a medium cup it would be 15Rs")

elif cup_size == "large":
    print("For a large cup it would be 20Rs")

else:
    print("Sorry we don't serve this size")