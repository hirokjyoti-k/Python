def square_num(*args):
    num = 1
    for i in args: 
        num *= i
    return num

num = [1,2,3,4,5]

print(square_num(*num))