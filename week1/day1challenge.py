user = input("What is your name?")
if len(user) < 10:
    print("String is not long enough")
elif len(user) > 10:
    print("String is too long")
else:
    print("Perfect string")
    print("First character:", user[0])
    print("Last character:", user[-1])
    build = ""
    for char in user:
        build += char
        print(build)
print(user[::-1])





     

