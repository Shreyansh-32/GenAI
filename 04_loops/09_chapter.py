# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")

# standard_sizes = ["small", "medium", "large"]
# if (req_size := input("Enter the size : ")) in standard_sizes:
#     print(f"Serving {req_size} chai")
# else:
#     print(f"{req_size} not available")

flavors = ["Ginger", "Lemon", "Masala"]
print(f"Available flavors : {flavors}")

while (flavor := input("Choose the flavor of tea : ")) not in flavors:
    print(f"Sorry, {flavor} tea is not available")

print(f"Serving {flavor} chai")