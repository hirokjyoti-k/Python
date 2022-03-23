data = [5 , 4 , "Hello", 5.6, [1,2,3], "hi"]
counter = 0
#count the num of integers in data list
for x in data:
    if type(x) is int:
        counter += 1
print(counter)