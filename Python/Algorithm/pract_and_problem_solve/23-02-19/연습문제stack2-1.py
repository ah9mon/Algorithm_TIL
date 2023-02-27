infix = '2+3*4/5'
stack = []
rlt =''
for i in infix:
    if i.isdecimal():
        rlt += i
    
    else:
        stack.append(i)

while stack: # 스택이 빌 때까지
    rlt += stack.pop()
    
print(rlt)

for j in rlt:
    if j.isdecimal():
        stack.append(int(j))
    else:
        a = stack.pop()
        b = stack.pop()
        if j == '*':
            stack.append(b * a)
        elif j == '/':
            stack.append(b / a)
        else: 
            stack.append(b + a)

print(stack.pop())
            
            