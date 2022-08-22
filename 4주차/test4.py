a = "000629-3222222"
year=""
month=""
gender=""
year = year+a[0]+a[1]
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
