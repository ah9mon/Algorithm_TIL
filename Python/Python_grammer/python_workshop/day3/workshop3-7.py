numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]

numbers.sort()
print(numbers)
print(numbers[16])
if len(numbers) % 2 == 0:
    print(numbers[int(len(numbers)/2)-1],numbers[int(len(numbers)/2 + 1)-1])
else:
    print(numbers[int((len(numbers)+1)/2)-1])

