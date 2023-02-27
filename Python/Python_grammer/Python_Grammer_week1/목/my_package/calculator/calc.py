# calculator/tools.py

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2==0:
        a = '0으로 나눌 수 없습니다'
        return a
    return n1 / n2
