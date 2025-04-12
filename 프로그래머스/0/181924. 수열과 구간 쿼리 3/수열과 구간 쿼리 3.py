def solution(arr, queries):
    answer = arr
    for query in queries:
        a=arr[query[0]]
        b=arr[query[1]]
        answer[query[0]]=b
        answer[query[1]]=a
        
        
    return answer