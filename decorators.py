
#Decorators are used to add functionality to a function without changing the code of the orininal function

def decorator_function(input_funtion): #takes original function as a input
    def add_feature(): #add the original functionality to a function
        print("This is an addition to the function")
        input_funtion()
    return add_feature

def func1():
    print("This is function one")

func1 = decorator_function(func1) #return the Decorators functions
func1() #call the Decorators functions