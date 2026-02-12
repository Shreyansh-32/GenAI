def add_vat(price, vat_rate):
    return price + price * vat_rate * 0.01

orders = [(1, 100), (2, 59), (3, 159)]

for idx,price in orders:
    print(f"{idx} customer's final price is {add_vat(price, 10)}")