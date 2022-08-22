import datetime as dt

days = '월화수목금토일'
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_month = int(input('기념일 시작하는 월: '))    # 6
start_day = int(input('기념일 시작하는 일: '))      # 21
start_week = input('기념일 시작하는 요일("월화수목금토일"): ')        # '월'
after_day = int(input('기념하고자 하는 기간: '))    # 100


def after_100(start_month, start_day, start_week) :
    # 요일 찾기
    day_delta = after_day % 7     # 나머지 2
    idx = (days.index(start_week) + day_delta - 1) % 7
    finish_week = days[idx]
    # print(f'기념요일: {finish_week}요일')

    # 몇월 몇일 찾기
    day_sum = months[start_month - 1] - start_day + 1
    # print('day_sum :', day_sum)

    # 기념일이 시작 월에 있을 경우
    if after_day <= day_sum :
        print(f'{start_month}월 {start_day}일 {start_week}요일부터 {after_day}일 뒤는 {start_month}월 {start_day + after_day - 1}일 {finish_week}요일')

    # 기념일이 시작 월을 넘어가는 경우
    else :
        k = 0
        remaining_day = after_day - day_sum
        # print(f'{day_sum}지남  {start_month}월말 잔여일: {remaining_day}')
        while True :

            mm = (start_month + k ) % 12

            # 남은 일정이 1개월을 초과한 경우
            if remaining_day > months[mm + 1] :
                k = k + 1
                day_sum = day_sum + months[mm]
                remaining_day = after_day - day_sum
                # print(f'{day_sum}지남  {mm}월말 잔여일: {remaining_day}')
                continue

            # 남은 일정이 1개월 이내인 경우
            else :
                finish_month = mm + 1
                finish_day = after_day - day_sum
                print(f'{start_month}월 {start_day}일 {start_week}요일부터 {after_day}일 뒤는 {finish_month}월 {finish_day}일 {finish_week}요일')
                break


after_100(start_month, start_day, start_week)
