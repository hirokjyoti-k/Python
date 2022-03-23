# def average_function(l1,l2):
#     average = []
#     for x in zip(l1,l2):
#         average.append(sum(x)/len(x))
#     return average


# def average_function(*args):
#     average = []
#     for x in zip(*args):
#         average.append(sum(x)/len(x))
#     return average

average_function = lambda *args : [sum(x)/len(x) for x in zip(*args)]

print(average_function([1,2,3],[4,5,6],[7,8,9]))