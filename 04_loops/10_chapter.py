users = [
    {"id" : 1, "total" : 100, "cupon" : "P20"},
    {"id" : 2, "total" : 150, "cupon" : "F10"},
    {"id" : 3, "total" : 80, "cupon" : "P15"},
]

discounts = {
    "P20" : (0.2, 0),
    "F10" : (0.5, 0),
    "P15" : (0, 15)
}

for user in users:
    percent, fixed = discounts.get(user['cupon'] , (0,0))
    discount = user["total"] * percent + fixed
    print(f"{id} User, used cupon {user['cupon']} to receive a discount of {discount}")