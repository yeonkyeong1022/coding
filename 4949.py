from sys import stdin 


while True:
    flag = 'yes'
    paren = []
    msg = stdin.readline().rstrip()
    if msg == '.':
        break 
    for i in msg :
        if i == '('or i=='[':
            paren.append(i)
        elif i==')':
            if len(paren)==0:
                flag = 'no'
                break 
            elif paren.pop() != '(':
                flag = 'no'
                break
        elif i==']':
            if len(paren)==0:
                flag = 'no'
                break 
            elif paren.pop() != '[':
                flag = 'no'
                break
    if len(paren)!= 0:
        flag = 'no'
    print(flag)