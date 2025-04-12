def solution(arr):
    answer = []
    for i in range(11):
        n = 2**i
        if n>=len(arr):
            app_cnt = n-len(arr)
            answer = arr+[0]*app_cnt
            break
        else:
            pass
    return answer