import sys
sys.stdin = open("input_for_4865.txt","rt",encoding = "UTF8")

T = int(input())

def max_word(str1, str2):

    N = len(str1)
    M = len(str2)
    # str2에 str1[i] 잇을때마다 체크
    check = [0]*N
    for i in range(N):
        for j in range(M):
            if str2[j] == str1[i]:
                check[i] += 1 # 체크

    return max(check)


for i in range(1,T+1):
    str1 = input()
    str2 = input()
    print(f'#{i} {max_word(str1,str2)}')
