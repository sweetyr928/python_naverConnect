import random

def rcp(ans,com):
    if ans == '가위':
        user = 0;
    elif ans == '바위':
        user = 1;
    elif ans == '보':
        user = 2;

    if com == '가위':
        computer = 0;
    elif com == '바위':
        computer = 1;
    elif com == '보':
        computer = 2;

    if user == 0 :
        if computer==0:
            return '비김'
        elif computer==1:
            return '컴퓨터 승'
        else:
            return '나의 승'
    elif user == 1:
        if computer==0:
            return '컴퓨터 승'
        elif computer==1:
            return '비김'
        else:
            return '나의 승'
    else:
        if computer==0:
            return '컴퓨터의 승'
        elif computer==1:
            return '나의 승'
        else:
            return '비김'

my = input("가위 바위 보:")
com = random.randint(0, 2)

if com == 0:
    computer = '가위';
elif com  == 1:
    computer = '바위';
elif com  == 2:
    computer = '보';

print('나: ',my)
print('컴퓨터 :',computer)

print(rcp(my,computer))
