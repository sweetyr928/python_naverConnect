import random

me=[0,0,0]
comp=[0,0,0]

def rsp_advanced(num):

    for i in range (0,num):

        while True:

            my = input("가위 바위 보:")
            com = random.randint(0, 2)

            if my=='가위' or my=='바위' or my=='보':
                if com == 0:
                    computer = '가위';
                elif com  == 1:
                    computer = '바위';
                elif com  == 2:
                    computer = '보';
                print('나: ',my)
                print('컴퓨터 :',computer)

                print(rcp(my,computer))
                break

            else:
                print('잘못 입력하셨습니다!')

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
            me[1]=me[1]+1
            comp[1]=comp[1]+1
            return '비김'
        elif computer==1:
            me[2]=me[2]+1
            comp[0]=comp[0]+1
            return '컴퓨터 승'
        else:
            me[0]=me[0]+1
            comp[2]=comp[2]+1
            return '나의 승'
    elif user == 1:
        if computer==0:
            me[2]=me[2]+1
            comp[0]=comp[0]+1
            return '컴퓨터 승'
        elif computer==1:
            me[1]=me[1]+1
            comp[1]=comp[1]+1
            return '비김'
        else:
            me[0]=me[0]+1
            comp[2]=comp[2]+1
            return '나의 승'
    else:
        if computer==0:
            me[2]=me[2]+1
            comp[0]=comp[0]+1
            return '컴퓨터의 승'
        elif computer==1:
            me[0]=me[0]+1
            comp[2]=comp[2]+1
            return '나의 승'
        else:
            me[1]=me[1]+1
            comp[1]=comp[1]+1
            return '비김'


games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)
print('나의 전적:',me[0],'승',me[1],'무',me[2],'패')
print('컴퓨터의 전적:',comp[0],'승',comp[1],'무',comp[2],'패')
