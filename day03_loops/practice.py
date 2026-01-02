
# Exercise A -- Print Numbers

for i in range(1,11):
    print(i)


# Exercise B -- Loop Through Names

names = ["Mike", "Ana", "Luis", "Sofia"]

for name in names:
    print("Hello", name)


# Exercise C -- Even Numbers Only

numbers = [4, 7, 10, 15, 18, 21]

for number in numbers: 
    if number % 2 == 0:
        print(number)


# Exercise D -- Count 

count = 0
for i in range(10):
    count += 1

print("Final count:", count)