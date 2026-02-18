from functools import wraps
# Decorator for authorization check

def check_access(func):
    @wraps(func)

    def wrapper(role):
        if role != "admin":
            print("Access denied : Admins only!")
            return None
        else:
            return func(role)
        
    return wrapper

@check_access
def tea_inventory(role):
    print("Access granted to tea inventory")

# tea_inventory("user")
tea_inventory("admin")