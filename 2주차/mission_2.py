def yearly_payment(m):

    x = m*12

    if x<=1200:
        y=x-x*0.6
    elif x<4600:
        y=x-x*0.15
    elif x<8800:
        y=x-x*0.24
    elif x<15000:
        y=x-x*0.35
    elif x<30000:
        y=x-x*0.38
    elif x<50000:
        y=x-x*0.4
    else:
        y=x-x*0.42

    print("세전연봉: ",x,"만원")
    print("세후연봉: ",round(y),"만원")

monthly_payment = int(input("월급: "))
yearly_payment(monthly_payment)
