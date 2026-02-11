staff = [("Shreyansh", 21) , ("Govind", 22), ("Dooba" , 24)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible")
        break
else:
    print(f"No one is eligible")