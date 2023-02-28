# 0000000111100000011000000111

arr = list(map(int,input()))
N =  len(arr)
num = 0
for i in range(N):
    j = i % 7
    # print(arr[i] * (2**(6-j)))
    num += arr[i] * (2**(6-j))
    # print(num)
    if j == 6:
        print(num)