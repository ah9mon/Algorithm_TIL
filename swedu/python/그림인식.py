# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_pic = [list(map(int, readl().strip())) for _ in range(N)]
	return N, map_pic

# 입력받는 부분
N, map_pic = input_data()

# 여기서부터 작성

# 1. 무슨색 있는지 찾고 위치 저장
colors = [0 for _ in range(10)]
colors_coor = [[(11,11),(-1,-1)] for _ in range(10)]

def find_size(r, c, color) :
	y1, x1 = colors_coor[color][0]
	y2, x2 = colors_coor[color][1]
	if (y1 > r) : y1 = r
	if (y2 < r) : y2 = r
	if (x1 > c) : x1 = c
	if (x2 < c) : x2 = c
	
	colors_coor[color][0] = (y1, x1)
	colors_coor[color][1] = (y2, x2)

def find_color() :
	global N
	for r in range(N) :
		for c in range(N) :
			color = map_pic[r][c]
			if (color != 0) :
				if (colors[color] == 0) :
					colors[color] = 1
				
				find_size(r,c, color)

find_color()

# 각 색의 범위안에 다른 색 있는지 찾기 
check = [0 for _ in range(10)]
for color in range(1, 10) :
	if (colors[color] == 1) :
		y1, x1 = colors_coor[color][0]
		y2, x2 = colors_coor[color][1]
		for r in range(y1, y2 + 1) :
			for c in range(x1, x2 + 1) :
				clr = map_pic[r][c]
				
				# 다른 색이면 덧칠한거임 
				if (clr != color) :
					check[clr] = 1

count = 0
for color in range(1,10) :
	if (colors[color] == 1 and check[color] == 0) :
		count += 1

# 출력하는 부분
print(count)