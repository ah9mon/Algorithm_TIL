#유성 
'''
https://www.acmicpc.net/problem/10703

'''

# 사진의 크기 
r,s = map(int,input().split())

# 사진 입력 받기 
selfie = [input() for _ in range(r)]
me = [-1]*s
gr = [-1]*s
# 각 column에서 X와 #의 최소 거리 찾기 
min_distance = r+1
for col in range(s):
    meteor = -1
    for row in range(r-1):
               
        if selfie[row][col] == 'X' and selfie[row+1][col] == '.': #운석 다음 공기면 그 줄의 운석의 끝
            me[col] = row
        
        if selfie[row][col] == '.' and selfie[row+1][col] == '#': # 공기 다음 운석이면 
            gr[col] = row + 1 
            if me[col] == -1: 
                break
            # print(gr[col], me[col])
            min_now = gr[col] - me[col] - 1
            if min_distance > min_now:
                min_distance = min_now                           
            break
# print(me)
# print(gr)
# print(min_distance)
# 공기 뺴기 
newpic = [['.']*s for _ in range(r)]
for col2 in range(s):
    counts = 0
    if me[col2] >= 0:
        for row2 in range(min_distance, min_distance + me[col2] + 1):
            newpic[row2][col2] = selfie[row2-min_distance][col2]
            
    if gr[col2] >= 0:
        for row3 in range(r-1,gr[col2]-1,-1):
   
            newpic[row3][col2] = selfie[row3][col2]

for i in range(r):
    print(''.join(newpic[i]))