def solution(arr, k):
    answer = []
    for i in arr:
        if k%2!=0:
            i = i*k
        else:
            i+=k
        answer.append(i)
    return answer