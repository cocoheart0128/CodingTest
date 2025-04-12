def solution(arr, delete_list):
    for delete in delete_list:
        if delete in arr:
            arr.remove(delete)
    answer = arr
    return answer