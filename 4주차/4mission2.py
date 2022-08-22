def count_word(str,word):

    f = open("test.txt", 'w')
    f.write(str)
    f.close()

    sum=0

    f = open("test.txt", 'r')

    for line in f:
        if word in line:
            a=line.count(word)
            sum = sum + a

    return sum


a = """파이썬을 공부한 지도 1달이 되어가네요.
미션을 해결하기 위해서는 앞서 배운 문법들을 잘 이해하고 있어야 합니다.
지금까지 배운 내용들을 모두 활용하여 앞으로의 미션들도 잘 해결해 보시기 바랍니다."""

print(count_word(a, "을"))
