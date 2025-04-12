def solution(myString):
    arr=[]
    for i in myString:
        if i=='a':
            arr.append('A')
        elif i!='A' and i.isupper()==True:
            arr.append(i.lower())
        else:
            arr.append(i)
    answer = ''.join(arr)
    return answer