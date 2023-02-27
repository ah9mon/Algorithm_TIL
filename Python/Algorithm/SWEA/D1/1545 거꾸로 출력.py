a = int(input())

b = list(range(0,a+1))
         
for i in range(1, a+1):
    
    print(b[-i], end =" " )
    if i == a:
        print(b[0])
