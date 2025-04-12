def solution(arr, queries):
    for query in queries:
        a = query[0]
        b = query[1]
        
        for i in range(len(arr)):
            if i>=a and i<=b:
                arr[i]+=1
            else:
                arr[i]=arr[i]

    answer=arr
    return answer