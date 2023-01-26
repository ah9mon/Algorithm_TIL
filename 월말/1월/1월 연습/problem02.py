def over(scores):
    list_over60 = []
    for score in scores:
        if score >= 60:
            list_over60.append(score)
    return len(list_over60)
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
