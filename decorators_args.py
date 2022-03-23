from functools import wraps

def allow_data_type(data_type): #function to take arguments
    def decorator(func): #decorators function
        @wraps(func) #wrapper functions
        def wrapper(*args, **Kargs):
            if all([type(arg) == data_type for arg in args]):
                return func(*args, **Kargs)
            print("Invalid Arguments")
        return wrapper
    return decorator

@allow_data_type(str) #decorators with arguments (takes datatype)
def join_str(*args):
    string = ''
    for i in args:
        string += i
    return string

print(join_str("Hirok","jyoti"," ","Kalita"))
