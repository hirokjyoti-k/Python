vowels = ('a','e','i','o','u')
user_name = input("Enter your name: ").lower()
counter = 0

for x in vowels:
    if x in user_name:
        print(f"{x} : {user_name.count(x)}")
