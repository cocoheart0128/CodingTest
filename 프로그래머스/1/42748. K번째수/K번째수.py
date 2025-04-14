def solution(array, commands):
    answer = []
    for command in commands:
        #print(command)
        a=command[0]-1
        b=command[1]
        c=command[2]-1
        result=sorted(array[a:b])[c]
        answer.append(result)
    return answer