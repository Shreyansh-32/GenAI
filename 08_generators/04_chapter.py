# Yield from other generator

def local_chai():
    yield "Ginger chai"
    yield "Masala chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


# Closing a yield
def chai_order():
    try:
        order = yield "Waiting for the order..."
    except:
        print("Stall closed! No more chai...")

order = chai_order()
print(next(order))
order.close()