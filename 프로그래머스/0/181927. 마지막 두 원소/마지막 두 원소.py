def solution(num_list):
    l=len(num_list)
    if num_list[l-1]>num_list[l-2]:
        add_num=num_list[l-1]-num_list[l-2]
    else:
        add_num=num_list[l-1]*2
    print(add_num)
    # answer = 0
    num_list.append(add_num)
    answer = num_list
    return answer