# OX퀴즈 

'''
https://www.acmicpc.net/problem/8958

ox 퀴즈에서 
o로 문제를 맞은 경우 
그 문제의 점수는 그 문제까지 연속된 o의 개수가됨

ox퀴즈 결과의 점수는 ? 
예시 input 
"OOXXOXXOOO"
'''
T = int(input())
for _ in range(T):
    quiz = input() # 정답 여부 입력받기 
    p = [0] * len(quiz) # 점수 기록용
    if quiz[0] == 'O': # 만약 첫번째 문제가 맞았으면
        p[0] += 1 
    for i in range(1,len(quiz)): # 2번문제 부터 끝까지 정답여부 확인
        if quiz[i] == "O": # 정답이면
            p[i] = p[i-1] + 1 # 현재문제의 점수 = 이전의 점수 + 1
    
    print(sum(p))
            
