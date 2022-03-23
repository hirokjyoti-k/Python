def find_power(num, *args):
    power_list = [i**num for i in args]
    return power_list

num = [1,2,3,4,5,6]
print(find_power(3,*num))
    