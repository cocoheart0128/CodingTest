def solution(arr, queries):
    answer=[]
    for query in queries:
        a=query[0]
        b=query[1]
        c=query[2]
        
        new_arr = sorted(arr[a:b+1])
        for i in range(len(new_arr)):
            if new_arr[i]>c:
                answer.append(new_arr[i])
                break
            elif new_arr[i]<=c and new_arr[i]==new_arr[-1]:
                answer.append(-1)
            
    return answer