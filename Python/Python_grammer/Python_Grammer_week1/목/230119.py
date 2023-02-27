# def my_magic(n):
#     return n*10

# my_list = [1,2,3,4,5]

# map_obj = list(map(my_magic,my_list))
# print(map_obj)

#/////////////////////

# def odd(n):
#     return n % 2
# numbers = [1,2,3]
# result = list(filter(odd, numbers))
# print(result, type(result))

#//////////////////////////

# name_list = ['신동민', '서재현', '박영서', '이태성', '정예원', '이은석']
# age_list = [17,18,22,24,25,19]

# for each in zip(name_list, age_list):
#     print(each)

# #////////////////////////////

# print((lambda x : x * x )(4))
# rlt = (lambda x : x * x )(4)

# my_func = lambda n : n * 2
# print(my_func(2))

# map_obj = map(lambda x : x * 10 , [1,2,3])
# rlt = list(map_obj)

# print(rlt)

# def recur():
#     print('ㅇ')
#     recur()

# recur()

# def fac(n):
#     if n == 0: # 재귀를 언제 끝낼 것인지 꼭 정해줘야함
#         return 1

#     return n * fac(n-1) 

# print(fac(5))

 # 패킹 언패킹

# x, y =1, 3
# z = 1,2,3

# a, *b =1,2,3,4
# print(a)
# print(b)

# def my_sum(a, b, c):
#     return a + b + c

# num_list = [10, 20, 30]

# rlt = my_sum(*num_list)
# print(rlt)

# def test(*values) :
#     for value in values:
#         print(value)

# test(1)
# test(1, 2)
# test(1, 2, 3, 4)

# def my_sum(a, *agrs) :
#     rlt = 0
#     for value in agrs:
#         rlt += value
#     return rlt

# #print(my_sum()) #0
# print(my_sum(1, 2, 3)) #5

def test(*args,**kwargs) :
    print(kwargs, type(kwargs))
    print(args, type(args))
    kwargs['name']
    return kwargs

test(1,2,3,4, name = 'aidem', age = 21)    