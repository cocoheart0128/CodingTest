def solution(num_list):
    a=[]
    b=[]
    for i in num_list:
        if i%2==0:
            a.append(str(i))
        else:
            b.append(str(i))
    
    stra = ''.join(a)
    strb = ''.join(b)
    
    answer=int(stra)+int(strb)
    return answer