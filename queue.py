# 함수 선언 #
def push(X) :
    global queue
    queue.append(X)

def pop() :
    global queue
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[0])
        queue.pop(0)
def size() :
    global queue
    print(len(queue))

def empty() :
    global queue
    if len(queue) == 0 :
        print(1)
    else :
        print(0)
def front() :
    global queue
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[0])
def back() :
    global queue
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[-1])

## 전역 변수 선언 부분##
queue = []

## 메인 코드 부분##
if __name__ == "__main__" :
    for _ in range(int(input())) :
        Command = input()
        if Command[0:4] == 'push' :
            a, b = Command.split()
            b = int(b)
            push(b)
        elif Command == 'pop' :
            pop()
        elif Command == 'size' :
            size()
        elif Command == 'empty' :
            empty()
        elif Command == 'front' :
            front()
        elif Command == 'back' :
            back()

