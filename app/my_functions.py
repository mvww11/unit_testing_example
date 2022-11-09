def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# print(add(2,6))