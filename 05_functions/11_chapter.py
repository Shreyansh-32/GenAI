# Pure function
def pure_chai(cups):
    cups += 2
    print("This is a pure function becuase it doesn't change any gloabal variable") 

total_cups = 100

# Impure function -> This is not recommended
def impure_chai():
    global total_cups
    total_cups -= 10
    print("This is an impure function because it manipulates global variable")

pure_chai(10)
impure_chai()
print(total_cups)

# Recursive function
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print("The result is : ",fibonacci(6))


chai_types = ["Masala", "Kadak", "Ginger", "Kadak"]
# Lambda functions -> basically functions with no name also known as annonymous functions
filtered_chai = list(filter(lambda chai: chai!="Kadak", chai_types))
print("Filtered chai types : ",filtered_chai)