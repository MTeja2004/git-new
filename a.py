name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = 2025 - age + 100
print("Hello, " + name)
print("You will turn 100 years old in the year", year)
repeat = int(input("How many times should I print the message? "))
print(("You will turn 100 in the year " + str(year) + "\n") * repeat)

