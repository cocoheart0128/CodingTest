def solution(my_string, queries):
    str_list = list(my_string)
    
    for query in queries:
        a, b = query
        str_list[a:b+1] = str_list[a:b+1][::-1]
        
    return ''.join(str_list)