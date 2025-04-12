def solution(a, d, included):
    arr=[]
    for i in range(len(included)):
        if included[i]==True:
            arr.append(a+d*i)
    answer=sum(arr)
    return answer