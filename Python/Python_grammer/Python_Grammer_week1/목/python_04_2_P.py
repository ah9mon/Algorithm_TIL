students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

stu_dict = {}
for student in students: # 리스트의 모든 원소에 대해
    if student in stu_dict.keys(): # stu_dict에 student가 키값으로 존재한다면 
        stu_dict[student] += 1 # 벨류에 +1
    
    else : # stu_dict에 student가 없다면 
        stu_dict[student] = 1 # {student : 1} 추가
cap = max(stu_dict, key = stu_dict.get) #박해피
# print(stu_dict)
# print(stu_dict.items())
print(cap)
