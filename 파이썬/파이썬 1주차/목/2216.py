def pita(a,b):
    return a**2 + b**2 




def s_triangle():

    s_list = []
    s_triangle1 = s_list.append(int(input("첫번쨰 변 : "))) # 5인 경우
    s_triangle2 = s_list.append(int(input("두번쨰 변 : "))) # 4인 경우
    s_triangle3 = s_list.append(int(input("세번쨰 변 : "))) # 3인 경우
    s_list.sort() #[3,4,5]

    if s_list[0] == s_list[1] == s_list[2]: #세변이 같다면
        s ='정삼각형'
        return s

    elif s_list[0] == s_list[1] or s_list[0] == s_list[2] or s_list[1] == s_list[2]: # 두변이 같다면
        s = '이등변삼각형'
        return s

    elif pita(s_list[0],s_list[1]) == s_list[2]**2: # 피타고라스 정리를 만족하면
        s = '직각삼각형'
        return s
    

    elif sum(s_list[0:2]) <= s_list[2]  : # 작은 두변의 합이 긴 변보다 작다면
        s = '삼각형 아님'
        return s

    else :
        s = '삼각형'     
        return s_triangle

print(s_triangle())    