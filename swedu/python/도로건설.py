import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_cost = []
	for _ in range(N) :
		line = list(map(int, list(sys.stdin.readline().strip())))
		map_cost.append(line)
	return N, map_cost

# 입력받는 부분
N, map_cost = input_data()
	
# 여기서부터 작성
visited = [[2000 for _ in range(N)] for _ in range(N)]
def bfs() :
	global N
	dx = [0,0,-1,1]
	dy = [-1,1,0,0]
	q = deque()
	q.append((0,0))
	visited[0][0] = map_cost[0][0]
	while(q) :
		y,x = q.popleft()
		for dv in range(4) :
			nx = x + dx[dv]
			ny = y + dy[dv]
			if (0 <= nx < N and 0 <= ny < N) :
				# 이전 길보다 가격이 낮을때만 이동
				
				if (visited[y][x] + map_cost[ny][nx] < visited[ny][nx]) :
					q.append((ny,nx))
					visited[ny][nx] = visited[y][x] + map_cost[ny][nx]

bfs()

# 출력하는 부분
print(visited[N-1][N-1])
