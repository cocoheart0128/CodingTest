def solution(my_string, m, c):
    all_part = []
    num =int(len(my_string)/m)
    for i in range(num):
        part = my_string[i*m:(i+1)*m]
        all_part.append(part)
    
    answer = ''.join([i[c-1] for i in all_part])
        
    return answer