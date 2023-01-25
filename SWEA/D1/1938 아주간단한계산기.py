numbers = input() # a b 의 형태로 자연수 입력값 받음
numbers = numbers.split() # [a, b]
for index_num in range(len(numbers)): 
    numbers[index_num] = int(numbers[index_num]) # [int(a), int(b)]
    
print(f'{int(numbers[0] + numbers[1])}') #11
print(f'{int(numbers[0] - numbers[1])}') #5
print(f'{int(numbers[0] * numbers[1])}') #24
print(f'{int(numbers[0] / numbers[1])}') #2
