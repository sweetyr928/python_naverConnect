def find_even_number(a,b):

    numbers = [ i for i in range(a,b+1)]

    for i in numbers:
         if i%2==0 and i==(a+b)/2:
             print(i,' 짝수')
             print(i,' 중앙값')
         elif i%2==0:
             print(i,' 짝수')


n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)
