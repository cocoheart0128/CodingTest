def solution(arr, queries):
    answer = arr
    for query in queries:
        new_ar = []
        print(query)
        for i in range(len(answer)):
            if i>=query[0] and i<=query[1] and i%(query[2])==0:
                answer[i]+=1
            else:
                i
            new_ar.append(answer[i])
        answer = new_ar
                
    return answer