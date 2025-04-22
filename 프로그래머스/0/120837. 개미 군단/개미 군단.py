def solution(hp):
    a = int(hp/5)
    b = int((hp%5)/3)
    c = int((hp%5)%3)
    answer = int(a+b+c)
    return answer