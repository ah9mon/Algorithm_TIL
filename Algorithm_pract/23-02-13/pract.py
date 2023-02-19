# 스택 연습 

# def push(item, size):
#     global top
#     top += 1
#     if top == size :
#         print('overflow')
#     else:
#         stack[top] = item
    
# size = 10 
# stack = [0] * size
# top = - 1

# push(10, size)
# top += 1 # push(20)
# stack[top] = 20
# print(stack) 

# def pop():
#     global top
    
#     if top == -1 :
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top + 1]

# print(pop())

# if top > -1 : 
#     top -= 1
#     print(stack[top + 1])


#재귀

'''
# 재귀호출의 기본형 
f(i, k) # i : 단계, k : 목표
    if i == k : # 목표도달
        return
    else:
        f(i+1,k) # 다음단계
'''
def f(i,k):
    if i == k:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)
        
A = [10,20,30]
B = [0] * 3
f(0,3)