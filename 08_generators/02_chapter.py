# Infinite generators

def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

user1 = infinite_chai()
print("User 1 : ")
for i in range (5):
    print(next(user1))

user2 = infinite_chai()
print("User 2 : ")
for i in range (7):
    print(next(user2))