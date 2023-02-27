import sys
sys.stdin = open("input_for_pract2.txt")

for i in range(1,7):
    strin = input()
    print(f'#{i} {strin} {type(strin)}')

