import sys

def junhyun() :
    global n
    asset = n
    num_of_stock = 0
    for price in chart :
        if (price <= asset) :
            ea, rest = divmod(asset, price)
            asset = rest
            num_of_stock += ea
    
    return num_of_stock * chart[-1] + asset

def sungmin() :
    global n
    asset = n
    num_of_stock = 0
    count_up = 0
    count_down = 0
    for i in range(1,14):
        if (chart[i - 1] < chart[i]) :
            if (count_down) :
                count_down = 0
            count_up += 1
        elif (chart[i - 1] > chart[i]) :
            if (count_up) :
                count_up = 0
            count_down += 1
        else :
            count_up = 0
            count_down = 0

        if (count_up >= 3) :
            if (num_of_stock > 0) :
                asset += num_of_stock * chart[i]
                num_of_stock = 0

        elif (count_down >= 3) :
            ea, rest = divmod(asset, chart[i])
            num_of_stock += ea
            asset = rest

    
    return num_of_stock * chart[-1] + asset


n = int(sys.stdin.readline())
chart = list(map(int, sys.stdin.readline().split()))
BNP = junhyun()
TIMING = sungmin()

if (BNP < TIMING) :
    print("TIMING")
elif (BNP > TIMING) :
    print("BNP")
else :
    print("SAMESAME")