names = ["Shreyansh", "Govind", "Venky", "Dooba"]
bill = [50, 85, 100, 55]

for name, amnt in zip(names, bill):
    print(f"Order ready for {name} of amount {amnt}")