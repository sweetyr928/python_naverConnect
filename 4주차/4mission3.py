def wrong_guest_book(guest_book):
    idx = guest_book.find(",")
    if not guest_book[idx+1]=='0':
        return idx
    elif not guest_book[idx+4] =='-':
        return idx
    elif not len(guest_book[idx+1:])==13:
        return idx
    return 0
f = open('guestbook.txt')
for line in f:
    idx = wrong_guest_book(line.rstrip())
    if idx != 0:
        print(f'잘못 쓴 사람: {line[:idx]}')
        print(f'잘못 쓴 번호: {line[idx+1:]}')
