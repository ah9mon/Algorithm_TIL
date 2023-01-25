# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3

def count_vowels(word):
    vowels = ['a','e','i','o','u']
    count = 0
    for alpha in word:
        if alpha in vowels:
            count += 1
            
    print(count)
    return count

        
count_vowels('apple') #=> 2
count_vowels('banana') #=> 3