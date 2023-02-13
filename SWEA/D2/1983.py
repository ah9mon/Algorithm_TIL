# 조교의 성적 매기기 

'''
총 10개의 평점 A+ ~ D0
학점 비율은 모두 10%
 
총점 = 중간 35 + 기말 45 + 과제 20

'''
import sys
sys.stdin = open('input_for_1983.txt')

def what_is_your_grade(N,K,stu_info):
    '''
    K번째 학생의 학점을 반환하는 함수
    
    # param
    N : 학생수 (N % 10 == 0 / 10 <= N <= 100)
    K : 관심있는 학생 번호 (1 <= K <= N)
    stu_info : [[중간, 기말, 과제], [중간, 기말, 과제], .... ]
    '''
    grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'] # 학점 정보
    
    # [중간, 기말, 과제] 점수를 비율을 반영하여 [총점]으로 바꿈
    for i in range(N): 
        grade = 0.35*stu_info[i][0] + 0.45*stu_info[i][1] + 0.2*stu_info[i][2]
        stu_info[i] = grade
    
    # [[총점1][총점2][총점3]...]의 형태로 바꾼 것을 정렬하여 새로운 변수에 할당 
    stu_sort = sorted(stu_info, reverse= True)
    
    # 학점을 매기기 위해 stu_sort를 N/10개 씩 나눠서 새로운 리스트에 할당 
    j = 0
    stu_grade = []
    while j < 0.9*N:
        stu_grade.append(stu_sort[j : int(j + 0.1*N)])
        j += int(0.1*N) 

    # K번째 학생의 학점을 반환 
    for k in range(len(stu_grade)):
        if stu_info[K-1] in stu_grade[k]:
            return grades[k]        

T = int(input())

for i in range(1,T+1):
    N, K = map(int,input().split())
    stu_info = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{i} {what_is_your_grade(N, K, stu_info)}')