def square_function(l):
    square_list = []
    for x in l:
        square_list.append(x**2)
    return square_list

input_list = list(range(1,11))
print(square_function(input_list))

