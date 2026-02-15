def make_chai():
    return "Your masala chai is ready!"

returned_value = make_chai() # We can store returned value in a variable
print(returned_value)

# If you don't return anything it implicitly returns none
def chai_ready():
    print("Your masala chai is ready!")

print(chai_ready())


# We can early return from a function
def cups_left(total_cups):
    if total_cups == 0:
        return "Sorry, we are out of cups"
    return "We have "+str(total_cups)+" cups left"

print(cups_left(0))
print(cups_left(5))

# We can reutnrn multiple values from a function
def chai_analytics():
    return 20, 100

remaining, sold = chai_analytics()
print("Remaining : ",remaining)
print("Sold : ",sold)