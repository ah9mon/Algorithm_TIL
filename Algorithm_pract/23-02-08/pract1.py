# 문자열 뒤집기 
import sys
sys.stdin = open("input_for_pract1.txt")

# 역슬라이싱 이용
# T = int(input())

# for i in range(1,T+1):
#     string1 = input()
#     print(f'#{i} {string1[::-1]}')

# reversed or reverse 이용
T = int(input())

for i in range(1,T+1):
    string1 = input()
    reverse_string = reversed(list(string1)) # reversed는 반환을 해줌 
    print(type(reverse_string))
    print(f'#{i} {"".join(reverse_string)}')
