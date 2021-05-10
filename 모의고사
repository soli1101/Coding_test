def solution(answers):
    answer = []
    pattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    one = [ 1 if pattern[0][i%5] == an else 0 for i, an in enumerate(answers)]
    two = [ 1 if pattern[1][i%8] == an else 0 for i, an in enumerate(answers)] 
    thr = [ 1 if pattern[2][i%10] == an else 0 for i, an in enumerate(answers)]
    score = [sum(one), sum(two), sum(thr)]
    answer = [i+1 for i in range(len(score)) if score[i] == max(score)]
    return answer
