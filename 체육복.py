def solution(n, lost, reserve):
    for i in set(reserve):
        if i in set(lost):
            lost.remove(i)
            reserve.remove(i)

    for j in set(reserve):
        if j-1 in set(lost):
            lost.remove(j-1)
        elif j+1 in set(lost):
            lost.remove(j+1)

    return n - len(set(lost))
