import sys

def checkTrain() :
    global N
    count = 1
    for train in range(1, N) :
        isPass = True
        
        for otherTrain in range(train) :
            
            if (train_info[train] == train_info[otherTrain]) :
                isPass = False
                break
        
        if(isPass) :
            count += 1
    
    return count
        

N, M = map(int,sys.stdin.readline().strip().split())
train_info = [[0 for _ in range(20)] for _ in range(N)]
for _ in range(M) :
    order = list(map(int, sys.stdin.readline().strip().split()))
    train_num =  order[1] - 1
    if (len(order) == 3) :
        
        seat_num = order[2] - 1

        if (order[0] == 1) :
            if (train_info[train_num][seat_num] == 0) :
                train_info[train_num][seat_num] = 1
        else :
            if (train_info[train_num][seat_num] == 1) :
                train_info[train_num][seat_num] = 0
    
    else :
        newTrainInfo = [0 for _ in range(20)]
        if (order[0] == 3) :
            for i in range(19) :
                if (train_info[train_num][i]) : 
                    newTrainInfo[i + 1] = train_info[train_num][i]
    
        else :
            for i in range(1,20) :
                if (train_info[train_num][i]) : 
                    if (i - 1 >= 0) :
                        newTrainInfo[i - 1] = train_info[train_num][i]
        
        train_info[train_num] = newTrainInfo

print(checkTrain())