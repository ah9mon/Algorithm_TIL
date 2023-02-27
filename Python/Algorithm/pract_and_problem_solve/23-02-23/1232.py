import sys
sys.stdin = open('input_for_1232.txt')


def inorder(n):
    # global rlt
    if cal[n][1].isdecimal(): # 피연산자면 자식 없음
        return int(cal[n][1])

    else: #연산자면 2 자식 있음
        a = inorder(int(cal[n][2]))
        b = cal[n][1]
        c = inorder(int(cal[n][3]))
        if b == '-':
            return int(a - c)
        elif b == '+':
            return int(a + c)
        elif b == '/':
            return int(a / c)
        elif b == '*':
            return int(a * c)

for i in range(1,11):
    # 정점의 개수
    N = int(input())
    # 인덱스 = 정점 번호
    # [정점 번호, 연산자, 왼자식,, 오른자식]
    cal = [[]] + [input().split() for _ in range(N)]
    # print(cal)
    # rlt = 0
    print(f'#{i} {inorder(1)}')