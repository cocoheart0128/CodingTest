def solution(arr, intervals):
    answer = []
    for interval in intervals:
        a=interval[0]
        b=interval[1]+1
        for i in arr[a:b]:
            answer.append(i)
                
    return answer