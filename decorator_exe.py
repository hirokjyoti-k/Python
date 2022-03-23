import time
import functools

def cal_execution_time(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kargs):
        t1 = time.time()
        value = func(*args, **kargs)
        t2 = time.time()
        print(f"executed {t1-t2} secouds")
        return value
    return wrapper_func

@cal_execution_time
def main_func():
    print("Hello World")

@cal_execution_time
def sum(n1, n2):
    return n1 + n2

print(sum(5,10))