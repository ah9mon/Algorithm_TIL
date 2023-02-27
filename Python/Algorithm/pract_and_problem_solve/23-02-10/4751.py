import sys
sys.stdin = open('input_for_4751.txt')

def func1(string):
    # 1개인 경우 # 한 행 길이 : 5 # 문자가 있어야 하는 인덱스 (2)
    # 2개인 경우 # 한 행 길이 : 9 # 문자가 있어야하는 인덱스 (2,6)
    # 3개인 경우 # 한 행 길이 : 13
    # 4    "    # 한 행 길이 : 17
    # 5    "    # 한 행 길이 : 21 # 문자가 있어야하는 인덱스 (2, 6, 10, 14, 18)
    # n    "    # 한 행 길이 : n * 4 + 1 # 문자가 있어야 하는 인덱스 range(2, n * 4 + 1, 4)

    # 문자열이 있는 부분 만들기
    N = len(string) # 원본 문자열 길이 
    line_len = N * 4 + 1 # 처리 후 각 문자열 길이 
    string_location = list(range(2,line_len,4))
    # print(string_location) 
    str_deco = [['#'] * line_len for _ in range(5)]
    # print(str_deco)

    for i in range(line_len):

        if i % 2: # 홀수면
            str_deco[2][i] = '.' 

        else: # 짝수면
            if i in string_location:  # 문자열이 들어가야 하는 인덱스면            
                str_deco[2][i] = string[string_location.index(i)] # 그곳에 맞는 문자열 입력 
            str_deco[1][i], str_deco[3][i] = '.', '.'
       
        if str_deco[2][i] == '#' or str_deco[1][i] == '#':
            str_deco[0][i],str_deco[-1][i] = '.','.' 

    for index in str_deco:
        print(''.join(index))

T = int(input())

for i in range(1,T+1):
    str_list = list(input())
    func1(str_list)