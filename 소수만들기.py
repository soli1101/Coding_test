from itertools import combinations
def solution(nums):
    prime = list(range(1,3000))

    for i in range(3, 3000):
        for j in range(2, i):
            if i%j==0: 
                prime.remove(i)
                break

    per = [i for i in combinations(nums, 3) if sum(i) in prime]

    return len(per)
