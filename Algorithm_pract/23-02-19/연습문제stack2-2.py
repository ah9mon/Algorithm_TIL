a = list(range(1,11))
bit = [0] * 10
sum1 = 0

def part(i,k, sum1):
    if sum1 > 10:
        return
    
    if i == k :
        if sum1 == 10:
            for j in bit:
                if j:
                    print(j, end = ' ')
            print('')
    else:
        bit[i] = a[i]
        part(i+1, k, sum1 + a[i])
        bit[i] = 0
        part(i+1, k, sum1)
        
part(0, 10, sum1)