from datetime import datetime

def solution(date1, date2):
    date1_dt = datetime.strptime(''.join([str(i).zfill(2) for i in date1]), '%Y%m%d')
    date2_dt = datetime.strptime(''.join([str(i).zfill(2) for i in date2]), '%Y%m%d')
    
    if date1_dt < date2_dt:
        return 1
    else:
        return 0

    
    return answer