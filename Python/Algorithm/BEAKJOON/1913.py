import sys 

def male(num) :
    for i in range(1,N + 1) :
        if (i % num == 0) :
            switches[i - 1] = '1' if (switches[i - 1] == '0') else '0'

def female(num) :
    i = 0
    while (
        (0 < num - (i + 1) <= N)
        and (0 < num + (i + 1) <= N)
        and (switches[num - (i + 1) - 1] == switches[num + (i + 1) - 1])
    ) :
        i += 1
    
    for index in range(num - i, num + i + 1) :
        switches[index - 1] = '1' if (switches[index - 1] == '0') else '0'

N = int(sys.stdin.readline())
switches = list(sys.stdin.readline().split())
num_of_stu = int(sys.stdin.readline())
stu_info = [[0,0] for _ in range(num_of_stu)]
for i in range(num_of_stu) :
    stu_sex, switch_num = sys.stdin.readline().split()
    stu_info[i][0] = stu_sex
    stu_info[i][1] = switch_num

for info in stu_info :
    if (info[0] == '1') :
        male(int(info[1]))
    else :
        female(int(info[1]))

for i in range(N // 20 + 1):
    print(' '.join(switches[20 * i : 20 * (i + 1)]).strip())