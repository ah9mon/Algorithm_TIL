
def u_to_the_0_to_the_u(string):
    print(string, string[::-1])
    if string == string[::-1]:
        return 1
    else:
        return 0

T = int(input())
for i in range(1, T + 1):
    string = input()
    print(f'#{i} {u_to_the_0_to_the_u(string)}')
    