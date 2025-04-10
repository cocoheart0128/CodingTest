def solution(arr, n):
    chk_nm = len(arr)
    new_arr = []
    if chk_nm%2==0:
        for i in range(0,chk_nm):
            if i%2!=0:
                val = arr[i]+n
            else:
                val=arr[i]
            new_arr.append(val)
    else:
        for i in range(0,chk_nm):
            if i%2!=0:
                val = arr[i]
            else:
                val=arr[i]+n
            new_arr.append(val)
    return new_arr
            