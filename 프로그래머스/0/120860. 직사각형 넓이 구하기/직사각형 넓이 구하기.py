def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    width = max([x1,x2,x3,x4])-min([x1,x2,x3,x4])
    hight = max([y1,y2,y3,y4])-min([y1,y2,y3,y4])
    answer=width*hight
    return answer