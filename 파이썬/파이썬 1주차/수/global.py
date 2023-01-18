# x = '글로벌'

# def func1():

#     def func2():
#         print(x)

#     func2()

# func1()        

# #L E G D
# #L 에 X가 없음 -> E에 x가 없음 -> G에서 x가 있음 -> 출력


# x = '글로벌'

# def func1():
#     x = '인클로징'
#     def func2():
#         print(x)

#     func2()

# func1()        

# #L E G D
# #L 에 X가 없음 -> E에 x가 있음 -> 출력

# x = '글로벌'

# def func1():
#     x = '인클로징'
#     def func2():
#         x = '로컬'
#         print(x)

#     func2()

# func1()        

# #L E G D
# #L 에 X가 있음 -> 바로 출력

x = '글로벌'

def func1():
    x = '인클로징'
    def func2():
        global x # 글로벌 변수로 지정
        x = '로컬'
        

    func2()

func1()

print(x)



# def func1():
#     x = '인클로징'
#     def func2():
#         nonlocal x 
#         x = '로컬'
        
    
#     func2()
#     print(x)

# func1()

