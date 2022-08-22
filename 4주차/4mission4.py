def check_id(id):
    year=""
    month=""
    gender=""

    if id[6]=='-' and len(id)==14:

        year = year+id[0]+id[1]
        if year=='00':
            ans=input('2000년생 출생자 입니까? 맞으면 o 아니면 x: ')
            if ans=='x':
                print("잘못된 번호입니다.\n올바른 번호를 넣어주세요")
                quit()

        month = month+a[2]+a[3]
        if a[7]=='2' or a[7]=='4':
            gender="여자"
        elif a[7]=='1' or a[7]=='3':
            gender="남자"
        print(year,"년",month,"월 ",gender)

    else:
        print("잘못된 번호입니다.\n올바른 번호를 넣어주세요")


a = input("주민등록번호를 입력해주세요('-포함'):")
check_id(a)
