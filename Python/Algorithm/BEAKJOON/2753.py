import sys

def isYunYear(year) :

    if (year%400) :
        if ((not (year % 4)) and (year % 100)) :
            return 1
    else :
        return 1
    
    return 0

year = int(sys.stdin.readline())
print(isYunYear(year))

