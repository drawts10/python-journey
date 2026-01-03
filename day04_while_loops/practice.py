
# Exercise A -- Countdown

count = 5

while count >= 0:
    print(count)
    count -= 1 

print("Done")


# Exercise B -- Password Check

password = "python1234"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Access granted")


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