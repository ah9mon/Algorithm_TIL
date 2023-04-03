'''
7
7
2 4 7 9 11 19 23
'''

def binary_search():
    start = 0
    end = N-1
    while start <= end :

        center = (start + end) // 2 
        print(center)
        if key > arr[center] : 
            print('왼')
            start = center + 1
            
        elif key < arr[center] : 
            print('오')
            end = center - 1
            
        else:
            return f'{center}에 있음'
        
    return f'없음'
        
            
N = int(input()) # 배열의 크기 
key = int(input()) # 찾고자 하는 값
arr = list(map(int,input().split())) # 배열 
print(binary_search())
