import functools

def decorator_function(input_funtion): #takes original function as a input
    '''Decorator Function'''
    @functools.wraps(input_funtion)
    def add_feature(*args,**kargs): #add the original functionality to a function
        print("This is an addition to the function")
        return input_funtion(*args,**kargs)
    return add_feature


# Decorators with a class

class sample:
    def __init__(self):
        pass

    @decorator_function
    def func(self, msg):
        return msg

s = sample()
print(s.func("Hello Hirok"))