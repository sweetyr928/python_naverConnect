def count_prime_number(a,b):
    d=0
    for i in range(a,b+1):
        c=0
        for k in range(1,i+1):
            if i%k == 0:
                c+=1
        if c==2:
            d+=1 #약수가 두개(1,자기자신)
    print('소수개수 ',d)

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)
