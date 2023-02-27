# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def average(scores):
    sum_num = sum(scores) # 330 
    #print(len(scores)) # 4
    average_num = sum_num / len(scores) # 82.5

    return average_num
    


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5