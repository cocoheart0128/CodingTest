def solution(score):
    avg_score = [sum(l)/len(l) for l in score]
    sorted_avg_score = sorted(avg_score,reverse =True)
    answer = [sorted_avg_score.index(s)+1 for s in avg_score]
    return answer