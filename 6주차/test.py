member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

avg=[]

for i in range(0,6):
    sum=0
    avg.append(member_names[i])
    for j in range(0,12):
        sum+=member_records[i][j]
    avg.append(sum/12)

dict = dict()
dict = {avg[i]: avg[i + 1] for i in range(0, len(avg), 2)}

tmp = list()
for k, v in dict.items() :
    tmp.append( (v, k) )

tmp = sorted(tmp, reverse=True)

i=0
for val, key in tmp[:6] :
    if val>5 and i<2:
        print("보너스 대상자: ",key)
    i+1

print()

tmp = sorted(tmp)
j=0
for val, key in tmp[:6] :
    if val<3 and j<2:
        print("면담 대상자: ",key)
    j+1
