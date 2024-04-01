import sys

M = int(sys.stdin.readline())
init = pow(2, 21)
ans = init
for _ in range(M) :
    commend = sys.stdin.readline().strip()
    if (not (commend == 'all' or commend == 'empty')) :
        commend, n = commend.split()
        n = int(n)
        n2 = pow(2,n)
    if (commend == 'add') :
        if (not (ans & n2)) :
            ans += n2
    elif (commend == 'remove') :
        if (ans & n2) :
            ans -= n2
    elif (commend == 'check') :
        if (ans & n2) :
            print(1)
        else :
            print(0)
    elif (commend == 'toggle') :
        if (ans & n2) :
            ans -= n2
        else :
            ans += n2
    elif (commend == 'all') :
        ans = init - 1
    elif (commend == 'empty') :
        ans = init