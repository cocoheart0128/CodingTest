def dir(key):
    direct=[[0, 1],[0, -1], [1, 0], [-1, 0]]
    if key == 'up':
        x,y = direct[0]
    elif key == 'down': 
        x,y = direct[1]
    elif key == 'right': 
        x,y = direct[2]
    elif key == 'left': 
        x,y = direct[3]
    return x,y
def solution(keyinput, board):
    x,y=[0,0]
    lim_x,lim_y=board
    max_x = lim_x // 2
    max_y = lim_y // 2
    for key in keyinput:
        mv_x,mv_y = dir(key)
        if -max_x <= x + mv_x <= max_x:
                    x += mv_x
        if -max_y <= y + mv_y <= max_y:
            y += mv_y        
    answer=[x,y]  
    return answer