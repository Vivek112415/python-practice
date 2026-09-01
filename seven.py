
            # : Find the Second Largest Number
numbers = [10, 25, 8, 45, 30]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Largest number:", largest)
print("Second largest number:", second)