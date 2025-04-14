def solution(arr, query):
    for i in range(len(query)):
        if i%2==0:
            n = query[i]
            arr=arr[:n+1]
        else:
            n = query[i]
            arr = arr[n:]
    answer = arr
    return answer