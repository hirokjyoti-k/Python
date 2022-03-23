users = [
    {'name' : 'Hirok', 'age' : 22 },
    {'name' : 'Raju', 'age' : 24 },
    {'name': 'Vievk', 'age' : 23 }
]

print(sorted(users, key = lambda user : user['age'])) #advance sort
print(min(users, key = lambda itm : itm['age'])) #advance min

users_dict = {
    'user1' : {'name' : 'Hirok', 'age' : 22 },
    'user2': {'name' : 'Raju', 'age' : 24 },
    'user' :{'name': "Vievk", 'age' : 20 }
}

print(sorted(users_dict, key = lambda user : users_dict[user]['age']))
print(min(users_dict, key = lambda itm : users_dict[itm]['age'])) #advance min