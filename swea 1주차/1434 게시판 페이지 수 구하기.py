a = int(input('게시글의 총 갯수를 입력하세요:'))
b = int(input('한 페이지에 필요한 게시글 수를 입력하세요:'))

c = a // b
d = a % b
if d > 0 :
    print(c+1)
else :
    print(c)
