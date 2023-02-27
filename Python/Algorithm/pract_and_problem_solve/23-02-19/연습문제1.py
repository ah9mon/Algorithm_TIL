# 스택 구현하기 

# push
def push(list1, item):
    global top
    if top + 1 == size:
        print('overflow!')
    else:
        top += 1
        list1[top] = item

# pop
def pop(list1):
    global top
    if top == -1:
        print('empty!')
    else:
        top -= 1
        return list1[top + 1]

size = 10
stack = [0] * size
top = -1

for i in range(1,size+1):
    push(stack, i)
    print(stack)
    print(top)

push(stack, 11)

for i in range(size):
    print(pop(stack))

pop(stack)