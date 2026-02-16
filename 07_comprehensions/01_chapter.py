# List comprehensions

menu = [
    "Masala chai",
    "Iced lemon tea",
    "Green tea",
    "Ginger chai",
    "Iced peach tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print("Iced tea : ",iced_tea)

chai = [chai for chai in menu if "chai" in chai]
print("Chai : ", chai)