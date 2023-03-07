# 배
'''
https://www.acmicpc.net/problem/1092

크레인 N eo 
1분에 박스를 하나씩 배에 실을 수 있다

각 크레인은 무게 제한이 잇음 
모든 박스를 배로 옮기는데 드는 시간의 최솟값
'''
def func():
    rlt = 0
    if cranes[0] < weights[0]:
        return -1
    
    while weights:
        for crane in cranes:
            for weight in weights:
                if crane >= weight:
                    weights.remove(weight)
                    break
        
        rlt += 1

    return rlt
            
N = int(input())

# 크레인 무게제한 
cranes = list(map(int,input().split()))
cranes.sort(reverse = True)

# 박스 수
M = int(input())

# 박스의 무게 
weights = list(map(int,input().split()))
weights.sort(reverse = True)

print(func())     
                
            
                
                
                
                 
  

        
        
        
        
        
    