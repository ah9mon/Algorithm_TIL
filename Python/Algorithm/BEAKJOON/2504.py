import sys
from collections import deque

def isRight() :
    
    stack = deque()
    for i in range(len(commend)) :
        if (commend[i] == '(' or commend[i] == '[') :
            stack.append(commend[i])
        else :
            if (stack) :
                c = stack.pop()
                if (commend[i] == ')' and c != '(') :
                    stack.append(c)
                elif (commend[i] == ']' and c != '[') :
                    stack.append(c)
                    
            else :
                return False
            
    if (stack) :
        return False
    else :
        return True


commend = sys.stdin.readline().strip()

if (isRight()) :
    rlt = []
    for i in range(len(commend)) :
        if ( commend[i] == '(' or commend[i] == '[') :
            rlt.append('+')
            rlt.append('(')
            
            
        elif (commend[i] == ')') :
            
            if (commend[i - 1] == '(') :
                rlt.append('+')
                rlt.append('2')
                rlt.append(')')
            else :
                rlt.append(')')
                rlt.append('*')
                rlt.append('2')

        elif (commend[i] == ']') :
            
            if (commend[i - 1] == '[') :
                rlt.append('+')
                rlt.append('3')
                rlt.append(')')
            else :
                rlt.append(')')
                rlt.append('*')
                rlt.append('3')

    print(eval(''.join(rlt)))
else :
    print(0)