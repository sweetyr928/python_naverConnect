import random
def guess_numbers():

    ran=list()
    ans=list()
    correct=list()

    number = random.randint(0, 100)
    number1 = random.randint(0, 100)
    if number1==number:
        number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    if number2==number or number2==number1 :
        number2 = random.randint(0, 100)

    ran.append(number);ran.append(number1);ran.append(number2)
    ran.sort()

    i=1
    while True:
        print(i,"차 시도")
        guess=int(input("숫자를 예측해보세요:"))

        if guess in ans:
            print("이미 예측에 사용한 숫자입니다")
            print(i,"차 시도")
            guess=int(input("숫자를 예측해보세요:"))

        if guess in ran:
            print("숫자를 맞추셨습니다!")
            correct.append(guess)
            if(guess==ran[0]):
                print(guess,"는 최솟값입니다!")
            elif(guess==ran[1]):
                print(guess,"는 중간값입니다!")
            elif(guess==ran[2]):
                print(guess,"는 최대값입니다!")

        else:
            if i==5 or i==10:
                print(guess,"는 없습니다")
                if guess>ran[0] and guess<ran[1]:
                    print("최솟값은",guess,"보다 작습니다")
                elif guess<ran[0]:
                    print("최솟값은",guess,"보다 큽니다")
                elif guess>ran[2]:
                    print("최댓값은",guess,"보다 작습니다")
                elif guess<ran[2] and guess>ran[1]:
                    print("최댓값은",guess,"보다 큽니다")

        if len(correct)==3:
            print("게임종료\n",i,"번만에 예측 성공 ")
            exit()

        ans.append(guess)
        i+=1

guess_numbers()
