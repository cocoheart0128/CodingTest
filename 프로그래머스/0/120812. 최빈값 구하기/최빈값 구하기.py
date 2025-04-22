def solution(array):
    answer = 0
    
    s = list(set(array))
    dic = {}
    for i in s:
        cnt = array.count(i)
        dic[i]=cnt
    val = [k for k, v in dic.items() if v == max(dic.values())]
    if len(val)==1:
        answer = val[0]
    else:
        answer = -1
    return answer