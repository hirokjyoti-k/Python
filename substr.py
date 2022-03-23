full_str = "Hello"

print("The original string is : " + str(full_str))
  
# Get all substrings of string
# Using list comprehension + string slicing
# res = [string[i: j] for i in range(len(string))
#           for j in range(i + 1, len(string) + 1)]
# print("All substrings of string are : " + str(res))


sub_str = []
for i in range(len(full_str)):
    for j in range(i+1, len(full_str)+1):
        sub_str.append(full_str[i:j])

print(f"Sub Strings of {full_str} : \n{sub_str}")
