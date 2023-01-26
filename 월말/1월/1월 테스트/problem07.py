# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.


def calculator(*numbers):
    if len(numbers) == 1: # 입력값이 하나라면 (5)
        round1 = 3.14 * (numbers[0] ** 2) # 원의 넓이 = 78.5
        return round1

    elif len(numbers) == 2: # 입력값이 두개라면 (10, 20)
        if sum(numbers) % 2 != 0: # 만약 두 입력값의 합이 홀수라면
            trian1 = numbers[0] * numbers[1] / 2 # 삼각형의 넓이(두 입력값이 (밑변, 높이) 라고 가정)
            return trian1

        else: # 두 입력 값의 합이 짝수라면 (10 + 20 = 30 -> 짝수 )
            square1 = numbers[0] * numbers[1] # 사각형의 넓이(두 입력값이 (밑변, 높이)라고 가정)
            return square1 # 사각형의 넓이 = 200

    elif len(numbers) >= 3: # 입력값이 3개 이상 이라면 (10, 20, 30, 40 )
        sum_nums = sum(numbers) #모든 수의 합 = 100
        mean_nums = sum_nums / len(numbers) # 모든 수의 평균 = 25.0 (len(numbers) = 4)
        tuple_rlt = sum_nums, mean_nums, # (합, 평균) = (100, 25.0)
        return tuple_rlt

    elif len(numbers) == 0: # 입력값이 없다면
        return 0 # 0
    

    

    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0