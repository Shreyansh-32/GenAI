from functools import wraps

# Building a logger for a function with args and kwargs

def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Executing function : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished called function : {func.__name__}")
        return result
    
    return wrapper

@log_activity
def brew_chai(type , milk = "no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("Masala")