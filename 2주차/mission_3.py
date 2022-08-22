def grader(name,a):
    if a > 94:
        grade = 'A+'
    elif a > 89:
        grade = "A"
    elif a > 84:
        grade = "B+"
    elif a > 79:
        grade = "B"
    elif a > 74:
        grade = "C+"
    elif a > 69:
        grade = "C"
    elif a > 64:
        grade = "D+"
    elif a > 59:
        grade = "D"
    else:
        grade = "F"

    print("이름:",name)
    print("점수:",a)
    print("학점:",grade)

student = str(input('이름을 입력하시오:'))
result = int(input('점수를 입력하시오:'))

if result>100:
    print('점수를 100점 이하로 입력해주세요')
    quit()

else:
    grader(student, result)
