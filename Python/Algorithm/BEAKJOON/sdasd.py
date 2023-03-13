r, s = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(input())
# print(arr)
arr_ = list(map(list, zip(*arr)))
# print(arr_)
t = 9999
for lst in arr_:
    if '#' in lst and 'X' in lst:
        e = lst[::-1].index('X')
        if t > lst[::-1][:e].count('.'):
            t = lst[::-1][:e].count('.')
            
# print(min(k))   # 'X'와  '#' 사이의 간격이 가장 좁은 곳 기준으로 그대로 내림
pic = [['.'] * s for _ in range(r)]
for i in range(r):
    for j in range(s):
        if arr[i][j] == '#':
            pic[i][j] = '#'
        if arr[i][j] == 'X':
            pic[i+t][j] = 'X'
for x in pic:
    ans = ''.join(x)
    print(ans)