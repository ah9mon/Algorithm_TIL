#침투게획세우기 

'''
https://www.acmicpc.net/problem/1606

0 번 껍질 1 1 (각 번호에 들어가는 수의 개수 / 각 번호에 들어있는 수의 최대값)
1 번 껍질 6 7 
2 번 껍질 12 19
3 번 껍질 18 37
-> 1 + 6*(1+2+3+...+n) (n : 껍질 번호)

1+2+3+....+n 은
n이 짝수면 (n+1)*(n//2) == (1+2+3+...+n)
n이 홀수면 (n)*((n-1)//2) + n == (1+2+3+...+n-1) + n 

위의 식을 알면 해당 껍질의 최솟값과 최댓값을 알 수 있다 


1. 껍질 번호 찾아야함
1 + 6*(1+2+3+...+n-1) ~ 1+6*(1+2+3+...n) 사이 값 탐색하기 
몇번껍질에 속하는지 알면 1부터 샐 필요가 없음
n번 껍질엔 (이전 껍질의 최대값 + 1) 부터 (지금 껍질의 최대값)까지 있기 때문에 이 만큼만 탐색하면 되니까

** 껍질 번호 찾는 방법 **
(좌표에 힌트가 있다)
좌표가 둘다 0 이상이면 두개 합한게 껍질 번호 

둘중 하나만 음수면 음수의 절대값이 껍질 번호 

둘다 음수면 합의 절대값이 껍질 번호 


2. 이젠 해당 껍질의 최솟값(N)부터 +1 해가면서 입력받은 좌표와 같아질때까지 
(n-1,1) 부터 (+dy[i], dx[i]) 해주며 원숭이가 인지하는 번호를 찾으면 됨 
 
dx = [1,0,-1,-1,0,1]
dy = [-1,-1,0,1,1,0]

1부터 ~ N+n 까지 6각형 형대로 쌓여감  

(n-1,1) 부터 (y + dy[0], x + dx[0]) n개 만들고 (매 위치가 (y,x)라고 하자)
(y + dy[1], x + dx[1]) n개 만들고
...
(y + dy[5], x + dx[5]) n개 만들면 n번째 껍질이 끝남 

그니까 +1 할때마다 같이 count해서 n번 카운트하면 i += 1해줘서 방향을 변경하면됨 

'''

def func():
    # 껍질 번호 찾기 
    if x >= 0 and y >= 0: # 둘다 0 이상이면 
        n = x+y # 껍질 번호는 두 좌표의 합 
        
        # 0,0 이면 그냥 종료 
        if x == 0 and y == 0:
            return 1   
            
    elif (x >= 0 and y < 0) or (x < 0 and y>=0): # 둘중하나만 음수면 
        n = abs(min(x,y)) # 최소값의 절대값이 껍질번호
 
    elif x < 0 and y < 0: # 둘다 음수면 
        n = abs(x+y) # 두 좌표의 합의 절대값이 껍질 번호 
    
    # 방향 
    dx = [1,0,-1,-1,0,1]
    dy = [-1,-1,0,1,1,0]
    
    # 같은방향으로 n번 움직이면 방향을 변경해줘야해서 카운트를 이용해 그걸 셀거야
    counts = 1
    
    # n번째 껍질의 최솟값 부터 탐색할거니까 알아야겠지?
    b = n-1
    if b % 2: # 홀수면
        N = 2 + 6*((b)*((b-1)//2) + b )  # n번째 껍질의 최솟값 
    else: # 짝수면
        N = 2 + 6*((b+1)*(b//2))
 
    i = 0  # dx, dy의 인덱스 
    ny,nx = n-1,1 # 탐색 시작 좌표 (n번째 껍질의 시작 좌표 해당 좌표의 숫자는 위에서 구한 N의 초기값이다)
    
    while True:
        # n번 이동하면 방향 변경
        if counts == n:
            i += 1
            counts = 0
        
        # 입력 좌표와 같으면 (정답이면) 
        if (ny,nx) == (y,x):
            return N # 해당 좌표의 원숭이가 인식하는 방법을 출력 
        
        # 다음칸 확인 
        ny += dy[i]
        nx += dx[i]
        N += 1
        counts += 1
    
# 멍멍이 금고 위치 
y, x = map(int,input().split())
print(func())
    
    
        
     

    



