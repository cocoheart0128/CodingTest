def solution(num_list):
    answer = 0
    cnt_list=[]
    for num in num_list:
        cnt=0
        while num!=1:
            if num%2==0:
                num=num/2
                cnt+=1
            else:
                num=(num-1)/2
                cnt+=1
        cnt_list.append(cnt)
    answer = sum(cnt_list)
                
    return answer