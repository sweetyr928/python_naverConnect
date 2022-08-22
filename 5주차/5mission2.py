def grader(s, a):
    result=list()
    only=list()
    for i in range(0,len(s)):
        temp=s[i].split(',')
        test=temp[1]
        num=0
        for i in range(0,10):
            if(int(test[i])==a[i]):
                num=num+10
        temp.append(num)
        result.append(temp)
        only.append(num)

    only.sort(reverse=True)

    for j in range(0,len(s)):
        place=1;
        for k in range(0,len(s)):
            if result[j][2]!=only[k]:
                place+=1;
            else:
                result[j].insert(0,place)

    result.sort()

    for m in range(0,len(s)):
        print('학생:',result[m][1],'점수:',result[m][3],'점 등수: ',result[m][0],"등")


# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

grader(s,a)
