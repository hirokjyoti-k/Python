def reverse_function(l):
    reverse_list = []
    for x in range(len(l)):
        # pop_item  = l.pop()
        reverse_list.append(l.pop())
    return reverse_list
        
main_list = list(range(1,11))
print(reverse_function(main_list))