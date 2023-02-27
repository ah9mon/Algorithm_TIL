#내 이름은 몇일까

def get_secret_number(string):
    str_list = list(map(ord,string)) 
    str_sum = sum(str_list)
    return str_sum

print(get_secret_number('happy'))