def max(a):

    max_num = a[0] # 첫 원소를 최대로 가정

    for index1 in range(len(a)):
        if a[index1] > max_num :
            max_num = a[index1]


    return max_num




a = list(map(int,input().split())) #[55,7,78,12,42]

print(max(a))