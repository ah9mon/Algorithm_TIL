T = int(input()) # 1



for index_num1 in range(T):
    N = int(input()) # 3

    ci_ki_list = list(input().split() for i in range(N))
    
    rlt = []

    for index in (ci_ki_list):
        rlt.append((index[0] * int(index[1])))
    
    # rlt = ['AAAAAAAAAA', 'BBBBBBB', 'CCCCC']
    
    text_rlt = ''.join(rlt) #AAAAAAAAAABBBBBBBCCCCC
   

    #print(text_rlt)
    print(f'#{index_num1 + 1}', end = '\n')

    a = len(text_rlt) // 10
    #print(a)
    b = len(text_rlt) % 10
    #print(b)

    for count in range(a):
        print(text_rlt[count*10:(count+1)*10])
    
    print(text_rlt[-b:])

    # for index_num2 in range(len(text_rlt)):

    #     if (index_num2 + 1) % 10 == 0:
    #         print(text_rlt[index_num2], end='\n')
            
    #     else:
    #         print(text_rlt[index_num2], end='')
    










        
    