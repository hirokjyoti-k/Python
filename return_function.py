def outer_func(msg):
    def inner_func():
        print(f"Message is: {msg}")
    return inner_func
    
res = outer_func("Hello World")
res()