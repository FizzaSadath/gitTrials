with open("numbers.txt", "r") as file:
    contents = file.read()
numbers = [int(x) for x in contents.split()]
print("Sum is:", sum(numbers))
