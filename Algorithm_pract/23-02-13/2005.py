import sys
sys.stdin = open('input_for_2005.txt')

# 파스칼의 삼각형 
'''
크기가 N인 삼각형 만들기

규칙

1. 첫 번째 줄은 항상 숫자 1
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합 
'''

# 열 길이 == 2 *(N-1) + 1
# 행 길이 == N 
def tri(n):
    tri_list = [[0]*(2*n + 1) for _ in range(n)]
    tri_list[0][n] = 1
    for i in range(1,n): # 행
        for j in range(1,2*n): # 각 숫자들 = 자신의 왼쪽 위 + 오른쪽 위 
            tri_list[i][j] = tri_list[i-1][j-1] + tri_list[i-1][j+1]
    
    # 출력 
    for k in range(n):
        for l in range((2*n + 1)):
            if tri_list[k][l]:
                print(tri_list[k][l], end = ' ')
        print('')

T = int(input())
for i in range(1,T+1):
    N = int(input()) 
    print(f'#{i}')
    tri(N)



