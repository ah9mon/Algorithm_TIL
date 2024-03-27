import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	map_line = []
	for _ in range(R) :
		line = list(sys.stdin.readline().strip().split())
		map_line.append(line)
	return R, C, map_line


sol = -1
# 입력받는 부분
R, C, map_line = input_data()

# 여기서부터 작성
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def change_line_num(r,c) :
	global R,C
	visited = [[0 for _ in range(C)] for _ in range(R)]
	q = deque()
	q.append((r,c))
	visited[r][c] = 1
	map_line[r][c] = '2'
	while(q) :
		y,x = q.popleft()
		for dv in range(4) :
			ny = y + dy[dv]
			nx = x + dx[dv]
			if (0 <= nx < C and 0 <= ny < R) :
				if (visited[ny][nx] == 0 and map_line[ny][nx] == '1') :
					q.append((ny,nx))
					visited[ny][nx] == 1 
					map_line[ny][nx] = '2'

visited = [[2501 for _ in range(C)] for _ in range(R)]
def bfs(r,c) :
	global R,C
	q = deque()
	q.append((r,c))
	if (visited[r][c] == 2501) : visited[r][c] = 0
	while(q) :
		y,x = q.popleft()
		for dv in range(4) :
			ny = y + dy[dv]
			nx = x + dx[dv]
			if (0 <= nx < C and 0 <= ny < R) :
				if (map_line[ny][nx] == '0') :
					if (visited[ny][nx] > visited[y][x] + 1) :
						q.append((ny,nx))
						visited[ny][nx] = visited[y][x] + 1
				elif (map_line[ny][nx] == '2') :
					return

# 동 하나 '2'로 바꾸기
flag = 0
for r in range(R) :
	for c in range(C) :
		if (map_line[r][c] == '1') :
			change_line_num(r,c)
			flag = 1
			break
		
		if (flag) :
			break

for r in range(R) :
	for c in range(C) :
		if (map_line[r][c] == '1') :
			bfs(r,c)			
			
min_cost = 2501
for r in range(R) :
	for c in range(C) :
		if (map_line[r][c] == '2') :
			for dv in range(4) :
				nr = r + dy[dv]
				nc = c + dx[dv]
				if (0<= nc < C and 0 <= nr < R and map_line[nr][nc] == '0' and visited[nr][nc] != 2501) :
					if (min_cost > visited[nr][nc]) :
						min_cost = visited[nr][nc]
						
# 출력하는 부분
print(min_cost)
