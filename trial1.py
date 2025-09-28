numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
total = 0

for num in numbers:
    total += num

print("The sum is:", total)
