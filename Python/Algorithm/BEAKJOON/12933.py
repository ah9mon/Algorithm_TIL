import sys 

def getRlt() :
    global soundLen
    global count
    
    # 소리 잘못된 케이스
    if (soundLen % 5) : return -1

    for i in range(soundLen) :
        if (visited[i] and soundTrack[i] == 'q'):
            visited[i] = 0
            findDuck(i)

    # 소리 잘못된 케이스
    if (sum(visited)):
        return -1

    if (count) :
        return count
    else:
        return -1

def findDuck(index) :
    global count
    sound = 'quack'
    isDuck = False
    i = 1
    
    for j in range(index + 1, soundLen) :
        if (visited[j] and (soundTrack[j] == sound[i])) :
            visited[j] = 0
            if (i == 4) :
                i = 0
                if (not isDuck) :
                    isDuck = True
            else :
                i += 1
    
    count += 1 if isDuck else 0

soundTrack = list(sys.stdin.readline().strip())
soundLen = len(soundTrack)
visited = [1 for _ in range(soundLen)]
count = 0

rlt = getRlt()
print(rlt)