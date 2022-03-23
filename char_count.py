name = input("Enter your name: ").lower()
i = 0
temp_name = ""

while i < len(name):
    if(name[i] not in temp_name):
        temp_name += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1