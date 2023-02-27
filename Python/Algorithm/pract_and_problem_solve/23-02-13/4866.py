# 괄호 짝 검사 / 스택 연습 

def stack1(str1):
    stack = []
    for char in str1:
        if char == '(':
            stack.append(char)
        else:
            # pop()은 리스트가 비어있으면 오류 뜨므로 try / except 사용
            try : 
                stack.pop()
            except: # 스택이 비어있어서 pop()이 오류가 발생하면 
                return -1

    
    if stack: # 스택이 비어있지 않으면 
        return -1
    else: # 스택이 비어있으면 
        return 1

T = int(input())

for i in range(1,T+1):
    str1 = input()
    print(f'#{i} {stack1(str1)}')
