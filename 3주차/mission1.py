def gugudan(number):
    for i in range (1,9,2):
        ans=number*i
        if ans <= 50:
            print(number,'x',i,'=',number*i)
        else:
            break

number = int(input("몇 단? : "))
gugudan(number)
