def bus_fare(age,case):
    if age>74:
        money=0;
    elif age>19:
        if case == "현금":
            money=1300
        else:
            money=1200
    elif age>13:
        if case == "현금":
            money=1000
        else:
            money=720
    elif age>7:
        money=450
    else :
        money=0

    print("버스요금: ", money,"원")

try :
    customer=int(input("나이:"))
    choice=str(input("지불유형:"))

except:
    print("나이를 숫자로 입력해주세요")
    quit()

bus_fare(customer, choice)
