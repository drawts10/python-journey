
# Exercise A -- Countdown

count = int(input("Enter a number: "))

while count >= 0:
    print(count)
    count -= 1 

print("Done")


# Exercise B -- Password Check

user_input = input("Enter user: ")
password = input("Enter password: ")
password_length = 8

if len(password) < password_length:
    print("Password should be longer", password_length = 8)
else: 
    while user_input != password:
        print("Access granted")
        break
   


# Exercise C -- Skip Number

i = 1

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# Exercise D -- COntrolled Stop

while True:
    command = input("Type 'stop' to end: ")

    if command == "stop":
        break