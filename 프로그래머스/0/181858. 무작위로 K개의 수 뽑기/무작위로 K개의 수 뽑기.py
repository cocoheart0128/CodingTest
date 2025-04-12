def solution(arr, k):
    dup_arr=[]
    for i in arr:
        if i not in dup_arr:
            dup_arr.append(i)
            
    ##set 함수 사용 하면 리스트 안에 원소의 순서 썪어서 결과 나옴
    # dup_arr = list(set(arr))
    if len(dup_arr)>=k:
        answer = dup_arr[:k]
    else:
        answer = dup_arr+[-1]*(k-len(dup_arr))
    return answer