import pandas as pd
def solution(todo_list, finished):
    idx=[]
    for i in range(len(finished)):
        if finished[i] is False:
            idx.append(i)
    print(idx)
    answer = [todo_list[k] for k in idx]

    return answer