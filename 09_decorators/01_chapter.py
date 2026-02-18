# Decorators are wrapper functions used to wrap a function
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("AFter function runs")
    
    return wrapper

@decorator
def greet():
    print("Hello from the greet function()")

greet()
print(greet.__name__)