def solution(strArr):
    new_arr=[]
    for str in strArr:
        if "ad" not in str:
            new_arr.append(str)
        
    return new_arr