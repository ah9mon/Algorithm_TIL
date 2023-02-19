# 괄호 검사 

def check(a):
    stack = []
    for char in a:
        if char == '(':
            stack.append(char)
        else:
            stack.pop()
    
    if not stack:
        return 1
    else:
        return -1

a = input()

print(check(a))

