# fn_d(91) 
# 출력 예시 
# 101


def fn_d(n):
    #n_list = [int(i) for i in str(n)]
    
    n_list = list(map(int,list(str(n))))
    n_list.append(n)
    return sum(n_list)

# fn_d = lamda n : sum([int[i] for i in str(n)] + [n])
#print(type(fn_d))

rlt = fn_d(91)
print(rlt)
    




def is_selfnumber(n):
    for m in range(1, n+1):
        if fn_d(m) == n:
            return False
    return True        
        


print(is_selfnumber(31))