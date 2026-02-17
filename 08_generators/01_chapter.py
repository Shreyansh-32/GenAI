# Generator basics

def serve_chai():
    yield "Masala chai"
    yield "Ginger chai"
    yield "Lemon tea"

stall = serve_chai()
# Stores reference of the execution of generator
print(stall)
for chai in stall:
    print(chai)


def get_chai():
    return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

cup = get_chai_gen()
print("\n\n\n",cup)
print(next(cup))
print(next(cup))
print(next(cup))
# print(next(cup)) Gives error saying stop iteration