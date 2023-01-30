

def collatz(num, count = 0):
    
    if count > 500:
        return -1 
    
    elif num == 1:
        return count
    
    elif num % 2 == 0 :
        count += 1
        num = num /2
        #print(num)
        return collatz(num, count)
    elif num % 2 != 0 : 
        count += 1
        num = num * 3 + 1
        #print(num)
        return collatz(num, count)


print(collatz(6))  # => 8
print(collatz(16))  # => 4
print(collatz(27))  # => 111
print(collatz(626331))  # => -1