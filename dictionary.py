#Dictionary method 1
users = {
    "user1" : {
        "Name" :"Sample", 
        "Age" :52,
    },
     "user2" : {
        "Name" :"Hirok", 
        "Age" :22,
    }
}

for x in users:
    print(users[x]["Name"], end=" ")
    print(users[x]["Age"])
