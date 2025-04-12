def solution(my_string, indices):
    str_l = list(my_string) 
    for i in indices:
        str_l[i]=''
    print(str_l)
    answer = ''.join([str for str in str_l if str!=''])
    return answer