def solution(a, b, c, d):
    answer=0
    arr = [a,b,c,d]
    if len(list(set(arr)))==1:
        answer = a*1111
    elif len(list(set(arr)))==2 and arr.count(list(set(arr))[0])==2:
        answer = (list(set(arr))[0]+list(set(arr))[1])*abs((list(set(arr))[0]-list(set(arr))[1]))
    elif len(list(set(arr)))==4:
        answer = min(arr)
    elif len(list(set(arr)))==2 and arr.count(list(set(arr))[0])==1:
        answer = (10*list(set(arr))[1] +list(set(arr))[0])**2
    elif len(list(set(arr)))==2 and arr.count(list(set(arr))[1])==1:
        answer = (10*list(set(arr))[0] +list(set(arr))[1])**2
    else:
        a = list(set([x for x in arr if arr.count(x) == 1]))
        answer = a[0]*a[1]
                  
    return answer