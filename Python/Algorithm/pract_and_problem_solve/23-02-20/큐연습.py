
def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0]* 10
front = -1
rear = -1

enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())

from collections import deque

q1 = deque()
q1.append(1)
q1.append(2)
q1.append(3)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())