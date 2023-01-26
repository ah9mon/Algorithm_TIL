# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def over_24(people):
    people_over_24 = 0 
    for index_dict in people: #people 리스트 안의 원소(index_dict)마다
        if index_dict['age'] > 24: # index_dict의 ['age'] key값의 value가 24초과이면
            people_over_24 += 1 # people_over_24 = people_over_24 + 1
    return people_over_24
    


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4