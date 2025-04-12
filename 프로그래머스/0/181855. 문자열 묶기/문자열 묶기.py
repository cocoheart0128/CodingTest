def solution(strArr):
    ll = []
    for i in range(len(strArr)):
        ll.append(len(strArr[i]))
    
    cnt=0
    for k in list(set(ll)):
        aa = len([j for j in ll if j==k])
        if aa>=cnt:
            cnt = aa
        else:
            pass
    
        

        
        
    answer = cnt
    return answer