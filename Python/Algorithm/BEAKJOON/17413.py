import sys
from collections import deque

string = list(sys.stdin.readline().strip())

i = 0
stack = deque()
while (i < len(string)) :
    if (string[i] == '<') :
        while (i < len(string) and string[i] != '>') :
            i += 1
    elif (string[i] != ' ') :
        start = i
        while (i < len(string) and string[i] != ' ' and string[i] != '<') :
            stack.append(string[i])
            i += 1
        end = i

        for index in range(start, end) :
            string[index] = stack.pop()

    if (i < len(string) and string[i] != '<') :
        i += 1

print(''.join(string))