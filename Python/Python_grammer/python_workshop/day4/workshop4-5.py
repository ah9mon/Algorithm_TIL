#숫자의 의미
num_list = [83, 115, 65, 102, 89]

def get_secret_word(list1):
    new_list = list(map(chr,list1))
    new_word = ''.join(new_list)
    return new_word

print(get_secret_word(num_list))